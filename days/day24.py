from collections import defaultdict
from math import lcm

import common

DATA_FILE = 'day24.txt'
EXAMPLE_FILE = 'day24-example.txt'

DIRECTION_TRANSFORMATIONS = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
}


def parse_data(data):
    walls = set()
    blizzards = defaultdict(list)
    start_point = None
    finish_point = None
    directions = {
        '<': 'L',
        '^': 'U',
        '>': 'R',
        'v': 'D',
    }
    for i, line in enumerate(data, 1):
        if not line:
            break
        for j, char in enumerate(line, 1):
            point = (i, j)
            if char == '#':
                walls.add(point)
            elif char in directions:
                blizzards[point].append(directions[char])
            elif start_point is None:
                start_point = point
            else:
                finish_point = point

    return {
        'walls': walls,
        'blizzards': blizzards,
        'start_point': start_point,
        'finish_point': finish_point,
    }


def calculate_adjacents(point):
    return {
        (point[0] - 1, point[1]),
        (point[0], point[1] - 1),
        (point[0], point[1] + 1),
        (point[0] + 1, point[1]),
    }


def print_map(blizzards, walls, actual=None):
    min_x = min(p[0] for p in walls)
    max_x = max(p[0] for p in walls)
    min_y = min(p[1] for p in walls)
    max_y = max(p[1] for p in walls)

    blizzards

    print('=' * 20)
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            point = (i, j)
            char = '.'
            if actual and point == actual:
                char = 'E'
            elif point in walls:
                char = '#'
            elif point in blizzards:
                if len(blizzards[point]) >= 2:
                    char = len(blizzards[point])
                else:
                    char = blizzards[point][0]
            print(char, end='')
        print()
    print('=' * 20)


def regenerate_blizzard(old_blizzard, direction, walls):
    delta_x = 0
    delta_y = 0
    if direction in {'U', 'D'}:
        tmp_wall = set(p for p in walls if p[1] == old_blizzard[1])
        if direction == 'U':
            wall_point = max(tmp_wall)
            delta_x = -1
        else:
            wall_point = min(tmp_wall)
            delta_x = 1
    else:
        tmp_wall = set(p for p in walls if p[0] == old_blizzard[0])
        if direction == 'L':
            wall_point = max(tmp_wall)
            delta_y = -1
        else:
            wall_point = min(tmp_wall)
            delta_y = 1
    return (wall_point[0] + delta_x, wall_point[1] + delta_y)


def new_turn(blizzards, walls):
    new_blizzards = defaultdict(list)
    for point, directions in blizzards.items():
        for direction in directions:
            transf = DIRECTION_TRANSFORMATIONS[direction]
            new_point = (point[0] + transf[0], point[1] + transf[1])
            if new_point in walls:
                # Wall collision, regenerate blizzard
                new_point = regenerate_blizzard(new_point, direction, walls)
            new_blizzards[new_point].append(direction)

    return new_blizzards


def action_options(actual, blizzards_after_move, walls, finish_point):
    options = []

    adjacents = calculate_adjacents(actual) if actual not in walls else {(actual[0] + 1, actual[1])}

    if finish_point in adjacents:
        return [finish_point]

    # Move
    for point in adjacents:
        if point in walls:
            continue
        if point in blizzards_after_move:
            continue
        options.append(point)

    # Wait
    if actual not in blizzards_after_move:
        options.append(actual)

    return options


def precalculate_blizzards(blizzards, walls):
    min_x = min(p[0] for p in walls)
    max_x = max(p[0] for p in walls)
    min_y = min(p[1] for p in walls)
    max_y = max(p[1] for p in walls)

    num_cols = max_x - min_x - 1
    num_rows = max_y - min_y - 1

    num_differents_states = lcm(num_rows, num_cols)


    all_blizzards = []
    for i in range(num_differents_states):
        all_blizzards.append(blizzards)
        blizzards = new_turn(blizzards, walls)

    return all_blizzards


def do_the_thing(start, finish, all_blizzards, walls):
    explored = set()
    queue = []

    # Start point
    queue.append((start, 0))
    explored.add((start, 0 % len(all_blizzards)))

    while queue:
        current, minute = queue.pop(0)
        # print('current', current, 'minute', minute)
        # print_map(all_blizzards[minute % len(all_blizzards)], walls, current)

        next_minute = minute + 1
        next_blizzard_idx = next_minute % len(all_blizzards)
        blizzards_after_move = all_blizzards[next_blizzard_idx]
        options = action_options(current, blizzards_after_move, walls, finish)
        options = (p for p in options if (p, next_blizzard_idx) not in explored)
        # print('options', list(options))

        for option in options:
            queue.append((option, next_minute))
            explored.add((option, next_blizzard_idx))

            if option == finish:
                return next_minute


def foo(data):
    info = parse_data(data)
    walls = info['walls']
    blizzards = info['blizzards']
    start_point = info['start_point']
    finish_point = info['finish_point']

    # Add start point to walls to not going back
    walls.add(start_point)

    # print(start_point)
    # print(finish_point)
    # print(blizzards)

    all_blizzards = precalculate_blizzards(blizzards, walls)
    # print('all_blizzards', all_blizzards)
    # print('all_blizzards', len(all_blizzards))
    # for i, blizzards in enumerate(all_blizzards):
    #     print('i', i)
    #     print_map(blizzards, walls)

    result = do_the_thing(start_point, finish_point, all_blizzards, walls)
    print('result', result)
    return result


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return foo(data)


def part_2(input_file):
    raise NotImplementedError
