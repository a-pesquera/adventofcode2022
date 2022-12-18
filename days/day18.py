import common

DATA_FILE = 'day18.txt'
EXAMPLE_FILE = 'day18-example.txt'


def parse_line(line):
    return tuple(int(n) for n in line.split(','))


def cube_distance(cube1, cube2):
    return abs(cube1[0] - cube2[0]) + abs(cube1[1] - cube2[1]) + abs(cube1[2] - cube2[2])


def are_adjacent(cube1, cube2):
    if abs(cube1[0] - cube2[0]) >= 2:
        return False
    if abs(cube1[1] - cube2[1]) >= 2:
        return False
    if abs(cube1[2] - cube2[2]) >= 2:
        return False
    return abs(cube1[0] - cube2[0]) + abs(cube1[1] - cube2[1]) + abs(cube1[2] - cube2[2]) == 1


def count_surfaced_area(data):
    cubes = []
    for line in data:
        actual_cube = parse_line(line)
        # print('actual_cube', actual_cube)
        exposed_sides = 6
        for cube_row in cubes:
            cube = cube_row[0]
            # print('cube', cube)
            if are_adjacent(actual_cube, cube):
                exposed_sides -= 1
                cube_row[1] -= 1
        cubes.append([actual_cube, exposed_sides])

    # print(cubes)

    return sum(x[1] for x in cubes)


def find_mins_and_maxes(droplet):
    initial_cube = next(iter(droplet))
    min_x = max_x = initial_cube[0]
    min_y = max_y = initial_cube[1]
    min_z = max_z = initial_cube[2]

    for cube in droplet:
        min_x = min(min_x, cube[0])
        max_x = max(max_x, cube[0])

        min_y = min(min_y, cube[1])
        max_y = max(max_y, cube[1])

        min_z = min(min_z, cube[2])
        max_z = max(max_z, cube[2])

    return {
        'min_x': min_x,
        'max_x': max_x,
        'min_y': min_y,
        'max_y': max_y,
        'min_z': min_z,
        'max_z': max_z,
    }


def point_adjacent_to_droplet(cube, droplet):
    candidates = [
        (cube[0], cube[1], cube[2] + 1),
        (cube[0], cube[1], cube[2] - 1),
        (cube[0], cube[1] + 1, cube[2]),
        (cube[0], cube[1] - 1, cube[2]),
        (cube[0] + 1, cube[1], cube[2]),
        (cube[0] - 1, cube[1], cube[2]),
    ]

    return [p for p in candidates if p in droplet]


def point_is_exterior(cube, droplet, mins_and_maxes):
    # First, x from left to right
    for x in range(mins_and_maxes['min_x'], cube[0]):
        test_point = (x, cube[1], cube[2])
        if test_point in droplet:
            break
    else:
        return True

    # Second, x from right to left
    for x in range(cube[0] + 1, mins_and_maxes['max_x'] + 1):
        test_point = (x, cube[1], cube[2])
        if test_point in droplet:
            break
    else:
        return True

    # Then the same for y
    for y in range(mins_and_maxes['min_y'], cube[1]):
        test_point = (cube[0], y, cube[2])
        if test_point in droplet:
            break
    else:
        return True

    for y in range(cube[1] + 1, mins_and_maxes['max_y'] + 1):
        test_point = (cube[0], y, cube[2])
        if test_point in droplet:
            break
    else:
        return True

    # And finally for z
    for z in range(mins_and_maxes['min_z'], cube[2]):
        test_point = (cube[0], cube[1], z)
        if test_point in droplet:
            break
    else:
        return True

    for z in range(cube[2] + 1, mins_and_maxes['max_z'] + 1):
        test_point = (cube[0], cube[1], z)
        if test_point in droplet:
            break
    else:
        return True

    return False


def count_exterior_surfaced_area(data):
    cubes = []
    droplet = set()
    for line in data:
        actual_cube = parse_line(line)
        droplet.add(actual_cube)

    print('droplet', droplet)
    mins_and_maxes = find_mins_and_maxes(droplet)
    print('mins_and_maxes', mins_and_maxes)

    wrapper_cube = []  # [x][y][z]
    wrapper_x_from = mins_and_maxes['min_x'] - 1
    wrapper_x_to = mins_and_maxes['max_x'] + 1
    wrapper_y_from = mins_and_maxes['min_y'] - 1
    wrapper_y_to = mins_and_maxes['max_y'] + 1
    wrapper_z_from = mins_and_maxes['min_z'] - 1
    wrapper_z_to = mins_and_maxes['max_z'] + 1

    result = 0
    for x in range(wrapper_x_from, wrapper_x_to + 1):
        # print('x', x)
        for y in range(wrapper_y_from, wrapper_y_to + 1):
            # print('y', y)
            for z in range(wrapper_z_from, wrapper_z_to + 1):
                # print('z', z)
                point = (x, y, z)
                # print('point', point)

                if point in droplet:
                    continue

                cubes_adjacents = point_adjacent_to_droplet(point, droplet)
                if not cubes_adjacents:
                    continue

                print('point', point)

                is_exterior = point_is_exterior(point, droplet, mins_and_maxes)
                if not is_exterior:
                    print('Not exterior point')
                    continue

                print('Exterior point!!')
                print('Adjacent to:', cubes_adjacents)
                result += len(cubes_adjacents)

    # print('droplet', droplet)
    # print('mins_and_maxes', mins_and_maxes)

    return result


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return count_surfaced_area(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return count_exterior_surfaced_area(data)
