import re

import common

DATA_FILE = 'day15.txt'
EXAMPLE_FILE = 'day15-example.txt'

PARSE_RE = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')


def parse_line(line):
    return tuple(int(x) for x in PARSE_RE.match(line).groups())


def manhattan_distance(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


def fill_no_beacons_area(no_beacons, sensor, distance):
    for n in range(distance + 1):
        x_from = sensor[0] - distance + n
        x_to = sensor[0] + distance - n
        for x in range(x_from, x_to + 1):
            no_beacons.add((x, sensor[1] + n))
            no_beacons.add((x, sensor[1] - n))


def fill_no_beacons_area_small(no_beacons, sensor, distance, row_y):
    if not (sensor[1] - distance <= row_y <= sensor[1] + distance):
        return

    distance_to_y = sensor[1] - row_y

    x_from = sensor[0] - distance + abs(distance_to_y)
    x_to = sensor[0] + distance - abs(distance_to_y)

    for x in range(x_from, x_to + 1):
        no_beacons.add((x, row_y))


def foo(data, check_y):
    beacons = set()
    no_beacons = set()

    for line in data:
        sx, sy, bx, by = parse_line(line)
        sensor = (sx, sy)
        beacon = (bx, by)
        # print('sensor', sensor, 'beacon', beacon)

        distance = manhattan_distance(sensor, beacon)
        beacons.add(beacon)

        fill_no_beacons_area_small(no_beacons, sensor, distance, check_y)
        if beacon in no_beacons:
            no_beacons.remove(beacon)

    result = set(p for p in no_beacons if p[1] == check_y)
    return len(result)


def part_1(input_file, check_y):
    data = common.read_data_file_generator(input_file)
    return foo(data, check_y)


def part_2(input_file):
    raise NotImplementedError
