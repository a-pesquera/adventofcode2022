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


def foo(data):
    cubes = []
    for line in data:
        actual_cube = parse_line(line)
        print('actual_cube', actual_cube)
        exposed_sides = 6
        for cube_row in cubes:
            cube = cube_row[0]
            print('cube', cube)
            if are_adjacent(actual_cube, cube):
                exposed_sides -= 1
                cube_row[1] -= 1
        cubes.append([actual_cube, exposed_sides])

    print(cubes)

    return sum(x[1] for x in cubes)


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return foo(data)


def part_2(input_file):
    raise NotImplementedError
