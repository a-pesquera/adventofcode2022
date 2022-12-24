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

    adjacents = calculate_adjacents(actual)

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


def precalculate_blizzards(blizzards, walls, top_left_point, bottom_right_point):
    num_cols = bottom_right_point[0] - top_left_point[0] + 1
    num_rows = bottom_right_point[1] - top_left_point[1] + 1

    num_differents_states = lcm(num_rows, num_cols)


    all_blizzards = []
    for i in range(num_differents_states):
        all_blizzards.append(blizzards)
        blizzards = new_turn(blizzards, walls)

    return all_blizzards


def do_the_thing(start, finish, all_blizzards, walls, initial_minute=0, print_things=False, return_path=False):
    explored = set()
    queue = []

    # Start point
    queue.append((start, initial_minute))
    explored.add((start, initial_minute % len(all_blizzards)))

    path = {}
    path[(start, initial_minute)] = None

    while queue:
        current, minute = queue.pop(0)
        if print_things:
            print('current', current, 'minute', minute)
            print_map(all_blizzards[minute % len(all_blizzards)], walls, current)

        next_minute = minute + 1
        next_blizzard_idx = next_minute % len(all_blizzards)
        blizzards_after_move = all_blizzards[next_blizzard_idx]
        options = action_options(current, blizzards_after_move, walls, finish)
        options = (p for p in options if (p, next_blizzard_idx) not in explored)
        if print_things:
            options = list(options)
            print('options', options)

        for option in options:
            queue.append((option, next_minute))
            explored.add((option, next_blizzard_idx))
            path[(option, next_minute)] = (current, minute)

            if option == finish:
                if return_path:
                    full_path = [option]
                    previous_key = (option, next_minute)
                    while path[previous_key]:
                        previous, time = path[previous_key]
                        full_path.append(previous)
                        previous_key = (previous, time)
                    return reversed(full_path)
                return next_minute


def foo(data, travels=1):
    info = parse_data(data)
    walls = info['walls']
    blizzards = info['blizzards']
    start_point = info['start_point']
    finish_point = info['finish_point']

    # Calculate rectangle dimensions
    min_x = min(p[0] for p in walls) + 1
    max_x = max(p[0] for p in walls) - 1
    min_y = min(p[1] for p in walls) + 1
    max_y = max(p[1] for p in walls) - 1
    top_left_point = (min_x, min_y)
    bottom_right_point = (max_x, max_y)

    # Close walls
    walls.add((start_point[0] - 1, start_point[1]))
    walls.add((finish_point[0] + 1, finish_point[1]))

    # All blizzards move the same way and after some minutes they are repeating the pattern
    all_blizzards = precalculate_blizzards(blizzards, walls, top_left_point, bottom_right_point)

    # Start travelling
    result = 0
    for i in range(travels):
        start, finish = start_point, finish_point

        if i % 2 != 0:
            # Go from end to start on odd travels
            start, finish = finish_point, start_point

        # Block start to not going back to square 1
        if finish in walls:
            walls.remove(finish)
        walls.add(start)

        result = do_the_thing(start, finish, all_blizzards, walls, initial_minute=result)

    return result


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return foo(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return foo(data, travels=3)
