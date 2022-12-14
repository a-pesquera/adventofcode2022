import common

DATA_FILE = 'day14.txt'
EXAMPLE_FILE = 'day14-example.txt'


def parse_path_of_rock(path_of_rock):
    # print('path_of_rock', path_of_rock)
    rocks = set()

    points = []
    for raw_point in path_of_rock.split(' -> '):
        x, y = tuple(int(x) for x in raw_point.split(','))
        points.append((x, y))

    current, *points = points
    rocks.add(current)

    for point in points:
        # print('current', current, 'point', point)
        while current != point:
            if current[0] == point[0]:
                # Vertical movement
                # print('V')
                if current[1] < point[1]:
                    # To the abyss
                    current = (current[0], current[1] + 1)
                else:
                    # To the sky
                    current = (current[0], current[1] - 1)
            else:
                # Horizontal movement
                # print('H')
                if current[0] < point[0]:
                    # Right
                    current = (current[0] + 1, current[1])
                else:
                    # Left
                    current = (current[0] - 1, current[1])
                pass
            # print('Adding current', current)
            rocks.add(current)

    return rocks


def generate_sand(start, rocks, limit=None):
    gravity = (0, 1)

    point = start

    # print('rocks', rocks)

    while True:
        point = (point[0] + gravity[0], point[1] + gravity[1])
        # print('sand', point)
        if limit and point[1] > limit:
            return None

        if point in rocks:
            # print('Boundary!! Trying to the left')
            left = (point[0] - 1, point[1])
            if left in rocks:
                # print('Left boundary!! Trying to the right')
                right = (point[0] + 1, point[1])
                if right in rocks:
                    stop_at = (point[0], point[1] - 1)
                    # print('Right boundary!! Stop this sand:', stop_at)
                    return stop_at
                else:
                    # print('Just air in right, continue')
                    point = (point[0] + 1, point[1] - 1)
            else:
                # print('Just air in left, continue')
                point = (point[0] - 1, point[1] - 1)


def units_of_sand(data, part=1):
    all_rocks = set()
    for path_of_rock in data:
        rocks = parse_path_of_rock(path_of_rock)
        all_rocks.update(rocks)

    # print('all_rocks', all_rocks)
    # print('all_rocks', len(all_rocks))

    last_rock_limit = max([x[1] for x in all_rocks])
    print('last_rock_limit', last_rock_limit)

    if part == 2:
        # Add floor rocks
        floor_y = last_rock_limit + 2

        lowest_x_coordinate = min([x[0] for x in all_rocks])
        highest_x_coordinate = max([x[0] for x in all_rocks])

        lowest_x_coordinate -= floor_y + 5  # Maybe only 1, but...
        highest_x_coordinate += floor_y + 5  # Maybe only 1, but...

        x_diff = highest_x_coordinate - lowest_x_coordinate + 1
        for i in range(x_diff):
            floor_point = (lowest_x_coordinate + i, floor_y)
            all_rocks.add(floor_point)

    sand_start = (500, 0)

    count_sand = 0
    limit = last_rock_limit if part == 1 else None
    while True:
        new_sand_point = generate_sand(sand_start, all_rocks, limit=limit)
        if new_sand_point is None:
            break
        all_rocks.add(new_sand_point)
        count_sand += 1
        if new_sand_point == sand_start:
            break

    return count_sand


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return units_of_sand(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return units_of_sand(data, part=2)
