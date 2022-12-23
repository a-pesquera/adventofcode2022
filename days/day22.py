import re

import common

DATA_FILE = 'day22.txt'
EXAMPLE_FILE = 'day22-example.txt'

DIRECTIONS = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0),
}

TURNS = {
    'R': {
        'R': 'D',
        'L': 'U',
        'U': 'R',
        'D': 'L',
    },
    'L': {
        'R': 'U',
        'L': 'D',
        'U': 'L',
        'D': 'R',
    },
}

DIRECTION_POINTS = 'RDLU'


def parse_data(data):
    first_row = 1
    first_col = 1
    last_row = 1
    last_col = 1

    start_point = None

    map_tiles = set()
    solid_walls = set()
    # off_the_map = set()

    for i, line in enumerate(data, 1):
        line = line.strip('\n')
        if not line:
            last_row = i - 1
            break

        last_col = max(last_col, len(line))
        for j, char in enumerate(line, 1):
            point = (i, j)
            if char == '.':
                map_tiles.add(point)
                if start_point is None:
                    start_point = point
            elif char == '#':
                map_tiles.add(point)
                solid_walls.add(point)
            # else:
            #     off_the_map.add(point)

    # # Create off the map for border
    # border_top_left = (first_row - 1, first_col - 1)
    # border_bottom_right = (last_row + 1, last_col + 1)
    # for n in range(border_top_left[1], (border_bottom_right[1]) + 1):
    #     off_the_map.add((border_top_left[0], n))
    #     off_the_map.add((border_bottom_right[0], n))
    # for n in range(first_row, last_row + 1):
    #     off_the_map.add((n, border_top_left[1]))
    #     off_the_map.add((n, border_bottom_right[1]))

    # Now instructions
    instructions_raw = next(data).strip('\n')
    parts = re.split(r'(\d+)', instructions_raw)
    parts.pop(0)
    instructions = []
    for num, turn in zip(parts[::2], parts[1::2]):
        instructions.append(int(num))
        if turn:
            instructions.append(turn)

    return {
        'start_point': start_point,
        'map_tiles': map_tiles,
        'solid_walls': solid_walls,
        # 'off_the_map': off_the_map,
        'instructions': instructions,
    }


def foo(data):
    info = parse_data(data)
    start_point = info['start_point']
    map_tiles = info['map_tiles']
    solid_walls = info['solid_walls']
    instructions = info['instructions']

    facing = 'R'
    actual = start_point
    # print('INITIAL', actual)

    for instruction in instructions:
        if isinstance(instruction, str):
            # Turn
            facing = TURNS[instruction][facing]
            # print('Turn to', facing)
        else:
            # Move
            # print('Move', instruction)
            movement = DIRECTIONS[facing]
            for _ in range(instruction):
                move_to = (actual[0] + movement[0], actual[1] + movement[1])

                # Check if limit reached to wrap around
                if move_to not in map_tiles:
                    if facing == 'R' or facing == 'L':
                        row = (x for x in map_tiles if x[0] == move_to[0])
                        new_move_to = min(row) if facing == 'R' else max(row)
                    else:
                        row = (x for x in map_tiles if x[1] == move_to[1])
                        new_move_to = min(row) if facing == 'D' else max(row)
                    # print(f'Wrap around from {move_to} to {new_move_to}')
                    move_to = new_move_to

                # Test movement
                if move_to in solid_walls:
                    # print(f'{move_to} is a wall - stop movement at {actual}')
                    break

                # Move
                actual = move_to

    print('facing', facing)
    print('actual', actual)
    return actual[0] * 1000 + 4 * actual[1] + DIRECTION_POINTS.index(facing)


def part_1(input_file):
    data = common.read_data_file_generator(input_file, strip=False)
    return foo(data)


def part_2(input_file):
    raise NotImplementedError
