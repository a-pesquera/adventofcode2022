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


def fill_no_beacons_area_small(sensor, distance, row_y, coverage_intervals):
    if not (sensor[1] - distance <= row_y <= sensor[1] + distance):
        return

    distance_to_y = sensor[1] - row_y

    x_from = sensor[0] - distance + abs(distance_to_y)
    x_to = sensor[0] + distance - abs(distance_to_y)
    # print('x_from', x_from)
    # print('x_to', x_to)

    coverage_intervals.append((x_from, x_to))


def do_the_thing(sensors_and_beacons, check_y, boundaries=None):
    beacons = set()

    coverage_intervals = []

    beacons_in_row_set = set()
    beacons_in_row = 0

    for sensor, beacon in sensors_and_beacons:
        distance = manhattan_distance(sensor, beacon)
        beacons.add(beacon)
        if beacon[1] == check_y and beacon not in beacons_in_row_set:
            beacons_in_row += 1
            beacons_in_row_set.add(beacon)
            # print('beacons_in_row', beacons_in_row)

        fill_no_beacons_area_small(sensor, distance, check_y, coverage_intervals)

    sted = sorted(coverage_intervals)
    new_intervals = []
    # print('sted', sted)
    for f, t in sted:
        # print('new_intervals', new_intervals)
        # print(f, t)
        if boundaries:
            f = max(f, boundaries[0])
            t = min(t, boundaries[1])
            # print('MODIFIED POINTS', f, t)
        fully_contained = False
        merge_with_index = None
        for i, (i_f, i_t) in enumerate(new_intervals):
            if i_f <= f and i_t >= t:
                fully_contained = True
                break
            if i_f <= f <= i_t or f <= i_t <= t:
                merge_with_index = i
                break

        if fully_contained:
            # print('fully_contained')
            continue

        if merge_with_index is not None:
            match_with = new_intervals.pop(merge_with_index)
            # print('merge:', match_with, (f, t))
            new_from = min(match_with[0], f)
            new_to = max(match_with[1], t)
            # print('new one', (new_from, new_to))
            new_intervals.append((new_from, new_to))
            continue

        new_intervals.append((f, t))

    return new_intervals, beacons_in_row


def foo(data, check_y):
    sensors_and_beacons = []
    for line in data:
        sx, sy, bx, by = parse_line(line)
        sensor = (sx, sy)
        beacon = (bx, by)
        print('sensor', sensor, 'beacon', beacon)
        sensors_and_beacons.append((sensor, beacon))

    new_intervals, beacons_in_row = do_the_thing(sensors_and_beacons, check_y)

    print('new_intervals', new_intervals)
    result = 0
    for interval in new_intervals:
        result += interval[1] - interval[0] + 1
    result -= beacons_in_row

    return result


def bar(data, limit):
    sensors_and_beacons = []
    for line in data:
        sx, sy, bx, by = parse_line(line)
        sensor = (sx, sy)
        beacon = (bx, by)
        # print('sensor', sensor, 'beacon', beacon)
        sensors_and_beacons.append((sensor, beacon))

    for check_y in range(limit):
        # print(check_y)
        new_intervals, _ = do_the_thing(sensors_and_beacons, check_y, boundaries=(0, limit))

        # print('new_intervals', new_intervals)
        result = 0
        for interval in new_intervals:
            if interval[1] < 0:
                continue
            elif interval[0] > limit:
                continue
            result += interval[1] - interval[0] + 1
        # print('result', result)
        if result != limit + 1:
            print('FOUND AT ROW', check_y, new_intervals)
            pos_x = new_intervals[0][1] + 1
            result_point = (pos_x, check_y)
            break

    result = result_point[0] * 4000000 + result_point[1]
    print('result', result)

    return result


def part_1(input_file, check_y):
    data = common.read_data_file_generator(input_file)
    return foo(data, check_y)


def part_2(input_file, limit=4_000_000):
    data = common.read_data_file_generator(input_file)
    return bar(data, limit)
