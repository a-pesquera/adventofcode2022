import string

import common

DATA_FILE = 'day3.txt'
EXAMPLE_FILE = 'day3-example.txt'


def find_error(rucksack):
    middle = len(rucksack) // 2
    compartment_left = set(rucksack[:middle])
    compartment_right = set(rucksack[middle:])
    in_both = compartment_left.intersection(compartment_right)
    return in_both.pop()


def find_common(rucksacks):
    in_all = set(rucksacks[0])
    for rucksack in rucksacks[1:]:
        in_all.intersection_update(set(rucksack))
    return in_all.pop()


def calculate_priority(item):
    index = string.ascii_letters.index(item)
    return index + 1


def calculate_sum_of_priorities(data):
    value = 0
    for rucksack in data:
        repeated_item = find_error(rucksack)
        priority_value = calculate_priority(repeated_item)
        value += priority_value
    return value


def calculate_sum_of_priorities_of_groups(data, group_size=3):
    value = 0
    group = []
    for rucksack in data:
        group.append(rucksack)

        if len(group) == group_size:
            full_group = group
            group = []

            repeated_item = find_common(full_group)
            priority_value = calculate_priority(repeated_item)
            value += priority_value

    return value


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return calculate_sum_of_priorities(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return calculate_sum_of_priorities_of_groups(data)
