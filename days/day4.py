import string

import common

DATA_FILE = 'day4.txt'
EXAMPLE_FILE = 'day4-example.txt'


def parse_line(pair):
    result = [int(n) for n in pair.replace(',', '-').split('-')]
    return result


def count_assignments(data, part=1):
    count = 0
    for pair in data:
        a1, a2, b1, b2 = parse_line(pair)
        a_set = set(range(a1, a2 + 1))
        b_set = set(range(b1, b2 + 1))
        if part == 1:
            # Fully contains
            # One set is a super set of the other
            if a_set >= b_set or a_set <= b_set:  # Same as a_set.issuperset(b_set) or b_set.issuperset(a_set):
                count += 1
        elif part == 2:
            # Partial overlap
            # One set contains at least 1 from the other
            if a_set & b_set:  # Same as a_set.intersection(b_set)
                count += 1
    return count


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return count_assignments(data, part=1)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return count_assignments(data, part=2)
