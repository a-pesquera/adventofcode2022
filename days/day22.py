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
    '180': {
        'R': 'L',
        'L': 'R',
        'U': 'D',
        'D': 'U',
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


def calculate_faces(up_face_point, other_faces_points, face_size):
    # @TODO generic transformation instead of hard-coded
    faces = {
        'U': up_face_point,
        'F': (51, 51) if face_size == 50 else (5, 9),
        'R': (1, 101) if face_size == 50 else (9, 13),
        'B': (151, 1) if face_size == 50 else (5, 1),
        'L': (101, 1) if face_size == 50 else (5, 5),
        'D': (101, 51) if face_size == 50 else (9, 9),
    }
    return faces


def parse_data_part_2(data, face_size):
    first_row = 1
    first_col = 1
    last_row = 1
    last_col = 1

    start_point = None
    up_face_point = None
    other_faces_points = []

    map_tiles = set()
    solid_walls = set()

    for i, line in enumerate(data, 1):
        line = line.strip('\n')
        if not line:
            last_row = i - 1
            break

        last_col = max(last_col, len(line))
        for j, char in enumerate(line, 1):
            point = (i, j)
            if char == '.' or char == '#':
                map_tiles.add(point)

                # Search faces
                if not up_face_point:
                    up_face_point = point
                elif abs(i - up_face_point[0]) % face_size == 0 and abs(j - up_face_point[1]) % face_size == 0:
                    other_faces_points.append(point)

                # Register walls and search starting point
                if char == '#':
                    solid_walls.add(point)
                elif start_point is None:
                    start_point = point

    # Now instructions
    instructions_raw = next(data).strip('\n')
    parts = re.split(r'(\d+)', instructions_raw)
    parts.pop(0)
    instructions = []
    for num, turn in zip(parts[::2], parts[1::2]):
        instructions.append(int(num))
        if turn:
            instructions.append(turn)

    # print('=' * 70)
    # for i in range(first_row, last_row + 1):
    #     for j in range(first_col, last_col + 1):
    #         point = (i, j)
    #         char = ' '
    #         if point in map_tiles:
    #             char = '#' if point in solid_walls else '.'
    #         print(char, end='')
    #     print()
    # print('=' * 70)

    # And ubicate faces
    faces = calculate_faces(up_face_point, other_faces_points, face_size)

    # print('other_faces_points', other_faces_points)

    return {
        'start_point': start_point,
        'map_tiles': map_tiles,
        'solid_walls': solid_walls,
        'instructions': instructions,
        'faces': faces,
    }


def bar(data, face_size):
    info = parse_data_part_2(data, face_size)
    start_point = info['start_point']
    map_tiles = info['map_tiles']
    solid_walls = info['solid_walls']
    instructions = info['instructions']
    faces = info['faces']
    print('faces', faces)

    if face_size == 4:
        """
        Example:
          U
        BLF
          DR
        """
        wrapping_dirt = {
            # FACEdirection -> NEW_FACEnew_direction
            # Uu -> Bd
            **{((1, 9 + n), 'U'): ((5, 4 - n), 'D') for n in range(face_size)},
            # Ul -> Ld
            **{((1 + n, 9), 'L'): ((5, 5 + n), 'D') for n in range(face_size)},
            # Ur -> Rl
            **{((1 + n, 12), 'R'): ((12 - n, 16), 'L') for n in range(face_size)},
            # Fr -> Rd
            **{((5 + n, 12), 'R'): ((9, 16 - n), 'D') for n in range(face_size)},
            # Rd -> Br
            **{((12, 13 + n), 'D'): ((8 - n, 1), 'R') for n in range(face_size)},
            # Dd -> Bu
            **{((12, 9 + n), 'D'): ((8, 4 - n), 'U') for n in range(face_size)},
            # Dl -> Lu
            **{((9 + n, 9), 'L'): ((8, 8 - n), 'U') for n in range(face_size)},
        }
    else:
        """
        File:
         UR
         F
        LD
        B
        """
        wrapping_dirt = {
            # 1 -> 1
            # 51 -> 5
            # 101 -> 9
            # 151 -> 13

            # 'U': (1, 51)     (1, 5)
            # 'F': (51, 51)    (5, 5)
            # 'R': (1, 101)    (1, 9)
            # 'B': (151, 1)    (13, 1)
            # 'L': (101, 1)    (9, 1)
            # 'D': (101, 51)   (9, 5)

            # FACEdirection -> NEW_FACEnew_direction
            # Uu -> Br
            # **{((1, 5 + n), 'U'): ((13 + n, 1), 'R') for n in range(face_size)},
            **{((1, 51 + n), 'U'): ((151 + n, 1), 'R') for n in range(face_size)},
            # Ul -> Lr
            # **{((1 + n, 5), 'L'): (((9 + face_size - 1) - n, 1), 'R') for n in range(face_size)},
            **{((1 + n, 51), 'L'): (((101 + face_size - 1) - n, 1), 'R') for n in range(face_size)},
            # Ru -> Bu
            # **{((1, 9 + n), 'U'): (((13 + face_size - 1), 1 + n), 'U') for n in range(face_size)},
            **{((1, 101 + n), 'U'): (((151 + face_size - 1), 1 + n), 'U') for n in range(face_size)},
            # Rr -> Dl
            # **{((1 + n, (9 + face_size - 1)), 'R'): (((9 + face_size - 1) - n, (5 + face_size - 1)), 'L') for n in range(face_size)},
            **{((1 + n, (101 + face_size - 1)), 'R'): (((101 + face_size - 1) - n, (51 + face_size - 1)), 'L') for n in range(face_size)},
            # Rd -> Fl
            # **{(((1 + face_size - 1), 9 + n), 'D'): ((5 + n, (5 + face_size - 1)), 'L') for n in range(face_size)},
            **{(((1 + face_size - 1), 101 + n), 'D'): ((51 + n, (51 + face_size - 1)), 'L') for n in range(face_size)},
            # Fl -> Ld
            # **{((5 + n, 5), 'L'): ((9, 1 + n), 'D') for n in range(face_size)},
            **{((51 + n, 51), 'L'): ((101, 1 + n), 'D') for n in range(face_size)},
            # Dd -> Bl
            # **{(((9 + face_size - 1), 5 + n), 'D'): ((13 + n, (1 + face_size - 1)), 'L') for n in range(face_size)},
            **{(((101 + face_size - 1), 51 + n), 'D'): ((151 + n, (1 + face_size - 1)), 'L') for n in range(face_size)},
        }


    def invert_wrapping_dict(wrapping_dirt):
        keys = list(wrapping_dirt.keys())
        for key in keys:
            key_point, key_dir = key
            val_point, val_dir = wrapping_dirt[key]
            wrapping_dirt[(val_point, TURNS['180'][val_dir])] = (key_point, TURNS['180'][key_dir])

    invert_wrapping_dict(wrapping_dirt)

    facing = 'R'
    actual = start_point

    for instruction in instructions:
        if isinstance(instruction, str):
            # Turn
            facing = TURNS[instruction][facing]
            print('Turn to', facing)
        else:
            # Move
            print('Move', instruction)
            for _ in range(instruction):
                movement = DIRECTIONS[facing]
                move_to = (actual[0] + movement[0], actual[1] + movement[1])

                # Check if limit reached to wrap around
                if move_to not in map_tiles:
                    print('actual', actual)
                    print('facing', facing)
                    print('move_to', move_to)
                    new_move_to, new_facing = wrapping_dirt[(actual, facing)]
                    if new_move_to not in solid_walls:
                        facing = new_facing
                        print('new_facing', new_facing)
                    print('new_move_to', new_move_to)
                    move_to = new_move_to

                # Test movement
                if move_to in solid_walls:
                    print(f'{move_to} is a wall - stop movement at {actual}')
                    break

                # Move
                actual = move_to

    print('facing', facing)
    print('actual', actual)
    return actual[0] * 1000 + 4 * actual[1] + DIRECTION_POINTS.index(facing)


def part_1(input_file):
    data = common.read_data_file_generator(input_file, strip=False)
    return foo(data)


def part_2(input_file, face_size=50):
    data = common.read_data_file_generator(input_file, strip=False)
    return bar(data, face_size)
