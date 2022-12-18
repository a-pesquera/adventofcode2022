import re
import itertools

import common

DATA_FILE = 'day16.txt'
EXAMPLE_FILE = 'day16-example.txt'

PARSE_RE = re.compile(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)')


class Node:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        self.open = False
        self.connections = []
        self.distances = {}

    def __repr__(self):
        status = '<OPEN>' if self.open else '<closed>'
        connections = ', '.join([f'({m}m to {n.name})' for n, m in self.connections])
        return f'{{Node {self.name} {status} (rate={self.rate}, connections={connections}, distances={self.distances})}}'

    def __hash__(self):
        return hash(self.name)

    def add_connection(self, node, minutes):
        self.connections.append((node, minutes))
        self.connections.sort(key=lambda x: x[0].name)

    def is_end(self):
        return len(self.connections) == 1

    def get_options(self, time_remaining):
        if time_remaining <= 0:
            return []

        options = []

        # First, open it
        if self.rate and not self.open:
            options.append(('OPEN',))

        # Second priority: move
        for node, minutes in self.connections:
            if node.open and node.is_end():
                continue
            options.append(('MOVE', minutes, node.name))

        return options

    def get_connected_node(self, name):
        lst = [node for node, _ in self.connections if node.name == name]
        return lst[0]

    def is_connected_to(self, node):
        st = set(x for x, _ in self.connections)
        return node in st

    def get_path(self, node, skip=None):
        if skip is None:
            skip = set()

        if self.is_connected_to(node):
            return [node.name]

        skip.add(self)

        path = []
        for conn, _ in self.connections:
            if conn in skip:
                continue
            found_path = conn.get_path(node, skip)
            print('?', conn, conn.get_path(node, skip))
        return path


def create_graph(data):
    valves = {}

    tmp = {}

    for line in data:
        name, rate, tunnels = PARSE_RE.match(line).groups()
        rate = int(rate)
        tunnels = tunnels.split(', ')
        valves[name] = Node(name, rate)
        tmp[name] = [(t, 1) for t in tunnels]

    check_valves = list(valves.values())
    for valve in check_valves:
        if valve.rate == 0 and len(tmp[valve.name]) == 2 and valve.name != 'AA':
            # print(valve)
            # print('this', tmp[valve.name])
            # print('Irrelevant connection')
            left, right = tmp[valve.name]
            # print('left, right', left, right)
            left_name = left[0]
            right_name = right[0]

            sum_minutes = left[1] + right[1]

            tmp[left_name] = [t for t in tmp[left_name] if t[0] != valve.name]
            tmp[left_name].append((right_name, sum_minutes))

            tmp[right_name] = [t for t in tmp[right_name] if t[0] != valve.name]
            tmp[right_name].append((left_name, sum_minutes))

            del valves[valve.name]
            del tmp[valve.name]

    for valve in valves.values():
        # print(valve.name)
        # print(tmp[valve.name])

        for name, minutes in tmp[valve.name]:
            valve.add_connection(valves[name], minutes)

    return valves


def calculate_distances(node, base_distance=0, skip_set=None, depth=1):
    if skip_set is None:
        skip_set = set()

    distances = {}

    processed = set()
    processed.update(skip_set)
    processed.add(node)
    # print((depth - 1) * '  ', f'Doing for {node.name}')

    for conn_node, conn_minutes in node.connections:
        if conn_node in processed:
            # print((depth - 1) * '  ', 'Skipping', conn_node.name)
            continue

        total_distance = base_distance + conn_minutes
        # print((depth - 1) * '  ', f'Distance to {conn_node.name} is {conn_minutes} what gives us a total of {total_distance}')
        if conn_node.name not in distances:
            distances[conn_node.name] = total_distance
        elif distances[conn_node.name] > total_distance:
            distances[conn_node.name] = total_distance
        else:
            # print((depth - 1) * '  ', f'Found another distance with less weight. Ignore this branch...')
            continue

        sub_distances = calculate_distances(conn_node, total_distance, processed, depth=depth + 1)
        for key, value in sub_distances.items():
            if key not in distances:
                distances[key] = value
            elif distances[key] > value:
                distances[key] = value

    # print((depth - 1) * '  ', f'Finish for {node.name}')
    # print((depth - 1) * '  ', 'RESULT DISTANCES', distances)
    return distances


def main_logic(actual, valves_remaining, time_remaining):
    best_path = [actual.name]
    best_score = 0

    for vr in valves_remaining:
        path = [actual.name]
        score = 0

        if actual.distances[vr.name] + 1 >= time_remaining:
            continue

        # Move
        tmp_time = time_remaining - actual.distances[vr.name]
        # Open
        tmp_time -= 1
        score += tmp_time * vr.rate

        other_valves = [x for x in valves_remaining if x != vr]
        tmp_score, tmp_path = main_logic(vr, other_valves, tmp_time)

        path.extend(tmp_path)

        score += tmp_score
        if score > best_score:
            best_score = score
            best_path = path

        # print('vr', vr)
        # print('score', score)
        # print('tmp_score', tmp_score)
        # print('path', path)

    return best_score, best_path


def foo(data, time_remaining=30, initial_valve='AA'):
    valves = create_graph(data)

    # Calculate distances from valve to all of other valves
    for name in valves:
        valves[name].distances = calculate_distances(valves[name])

    for name in valves:
        print(valves[name])

    valves_with_rate = [v for v in valves.values() if v.rate]
    print('valves_with_rate', len(valves_with_rate), valves_with_rate)

    best_score, best_path = main_logic(valves[initial_valve], valves_with_rate, time_remaining)
    print('best_score', best_score)
    print('best_path', best_path)
    return best_score

    # best_score = 0
    # best_path = None

    # for perm in itertools.permutations(valves_with_rate):
    #     # print([v.name for v in perm])
    #     time = time_remaining
    #     actual = valves[initial_valve]
    #     total_score = 0

    #     for v in perm:
    #         # Move to valve
    #         moving_time = actual.distances[v.name]
    #         time -= moving_time
    #         actual = v
    #         # print('moving_time', moving_time)
    #         # print('In valve', v.name)
    #         # print('time', time)
    #         v.open = True
    #         # print('Open valve', v.name)
    #         time -= 1
    #         score = time * v.rate
    #         # print('time', time)
    #         # print('score', score)
    #         total_score += score

    #     # print('total_score', total_score)
    #     if total_score > best_score:
    #         best_score = total_score
    #         best_path = perm

    # print('best_score', best_score)
    # print('best_path', [v.name for v in best_path])

    # return best_score


def bar(data, time_remaining=26, initial_valve='AA'):
    valves = create_graph(data)

    # Calculate distances from valve to all of other valves
    for name in valves:
        valves[name].distances = calculate_distances(valves[name])

    # for name in valves:
    #     print(valves[name])

    valves_with_rate = [v for v in valves.values() if v.rate]
    print('valves_with_rate', len(valves_with_rate), valves_with_rate)

    from itertools import permutations

    worker_1_length = len(valves_with_rate) // 2
    worker_2_length = len(valves_with_rate) - worker_1_length

    best_score = 0

    valves_with_rate_set = set(valves_with_rate)
    for tpl in permutations(valves_with_rate, worker_1_length):
        # print(tpl)
        valves_for_1 = set(tpl)
        # print('valves_for_1', valves_for_1)
        valves_for_2 = valves_with_rate_set - valves_for_1
        # print('valves_for_2', valves_for_2)

        best_score_1, best_path_1 = main_logic(valves[initial_valve], valves_for_1, time_remaining)
        best_score_2, best_path_2 = main_logic(valves[initial_valve], valves_for_2, time_remaining)
        # print('best_score_1', best_score_1)
        # print('best_path_1', best_path_1)
        # print('best_score_2', best_score_2)
        # print('best_path_2', best_path_2)
        if best_score_1 + best_score_2 > best_score:
            best_score = best_score_1 + best_score_2
            print('new best_score', best_score)

    print('best_score', best_score)

    return best_score

    # for _ in range(2):
    #     best_score, best_path = main_logic(valves[initial_valve], valves_with_rate, time_remaining)
    #     print('best_score', best_score)
    #     print('best_path', best_path)
    #     new_opened_valves = set(valves[name] for name in best_path)
    #     valves_with_rate = [x for x in valves_with_rate if x not in new_opened_valves]
    # return

    # num_workers = 2
    # times_workers = [(time_remaining, initial_valve)] * num_workers
    # print('times_workers', times_workers)

    # score = 0
    # while valves_with_rate and times_workers:
    #     print('Run loop')

    #     times_workers.sort(key=lambda x: x[0])
    #     worker_time_remaining, worker_valve_name = times_workers.pop()
    #     worker_valve = valves[worker_valve_name]

    #     print('worker_time_remaining, worker_valve_name', worker_time_remaining, worker_valve_name)

    #     _, best_path = main_logic(worker_valve, valves_with_rate, worker_time_remaining)

    #     if len(best_path) <= 1:
    #         continue

    #     print('valves_with_rate', valves_with_rate)
    #     print('best_path', best_path)

    #     next_valve_name = best_path[1]  # Second in best_path array
    #     next_valve = valves[next_valve_name]

    #     print('next_valve_name', next_valve_name, next_valve)

    #     # Move
    #     tmp_time = worker_time_remaining - worker_valve.distances[next_valve_name]
    #     # Open
    #     tmp_time -= 1
    #     score += tmp_time * next_valve.rate

    #     valves_with_rate = [x for x in valves_with_rate if x != next_valve]

    #     print('Final time', tmp_time)
    #     times_workers.append((tmp_time, next_valve_name))

    # print(score)

    # return score


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return foo(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return bar(data)
