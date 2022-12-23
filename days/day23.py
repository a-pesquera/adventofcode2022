import common

DATA_FILE = 'day23.txt'
EXAMPLE_FILE = 'day23-example.txt'


def calculate_adjacents(point):
    return {
        (point[0] - 1, point[1] - 1),
        (point[0] - 1, point[1]),
        (point[0] - 1, point[1] + 1),
        (point[0], point[1] - 1),
        (point[0], point[1] + 1),
        (point[0] + 1, point[1] - 1),
        (point[0] + 1, point[1]),
        (point[0] + 1, point[1] + 1),
    }


def count_ground_tiles(elves):
    min_x = min(p[0] for p in elves)
    max_x = max(p[0] for p in elves)
    min_y = min(p[1] for p in elves)
    max_y = max(p[1] for p in elves)
    ground = 0
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            point = (i, j)
            if point not in elves:
                ground += 1
    return ground


def plant_seeds(data, rounds=None):
    grove = set()
    elves = set()
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            point = (i, j)
            if char == '#':
                elves.add(point)

    priorities = [
        ('N', [(-1, -1), (-1, 0), (-1, 1)]),
        ('S', [(1, -1), (1, 0), (1, 1)]),
        ('W', [(-1, -1), (0, -1), (1, -1)]),
        ('E', [(-1, 1), (0, 1), (1, 1)]),
    ]

    n = 0
    while True:
        n += 1
        if rounds is not None and n > rounds:
            break

        separated_elves = set()
        moving_elves = set()
        for elf in elves:
            adjacents = calculate_adjacents(elf)
            neighbours = adjacents & elves
            if not neighbours:
                separated_elves.add(elf)
            else:
                moving_elves.add(elf)

        if not moving_elves:
            break

        propositions = {}
        for elf in moving_elves:
            for direction, points in priorities:
                check = set((elf[0] + p[0], elf[1] + p[1]) for p in points)
                check_result = check & elves
                if not check_result:
                    # Middle point is destiny
                    prop_point = (elf[0] + points[1][0], elf[1] + points[1][1])
                    if prop_point not in propositions:
                        propositions[prop_point] = []
                    propositions[prop_point].append(elf)
                    break

        for new_point, elf in propositions.items():
            if len(elf) >= 2:
                continue
            old_point = elf[0]
            elves.remove(old_point)
            elves.add(new_point)

        old_priority = priorities.pop(0)
        priorities.append(old_priority)

    return count_ground_tiles(elves), n


def part_1(input_file, rounds):
    data = common.read_data_file_generator(input_file)
    return plant_seeds(data, rounds)[0]


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return plant_seeds(data)[1]
