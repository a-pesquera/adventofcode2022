import string

import common

DATA_FILE = 'day4.txt'
EXAMPLE_FILE = 'day4-example.txt'


def parse_line(pair):
    result = []
    for elf in pair.split(','):
        result.append(tuple(int(n) for n in elf.split('-')))
    return tuple(result)


def count_assignments_fully_contains(data):
    count = 0
    for pair in data:
        section_assignment = parse_line(pair)
        elf_1, elf_2 = section_assignment
        if (elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]) or (elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]):
            count += 1
    return count


def count_assignments_overlaps(data):
    count = 0
    for pair in data:
        section_assignment = parse_line(pair)
        elf_1, elf_2 = section_assignment

        # Reorder if necessary
        if elf_2[0] < elf_1[0]:
            elf_1, elf_2 = elf_2, elf_1

        # Elf 1 is on the "left". Elf 2 on the "right". In case Elf 2 starts in
        # between Elf 1 work, there is an overlap.
        if elf_1[0] <= elf_2[0] <= elf_1[1]:
            count += 1
    return count


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return count_assignments_fully_contains(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return count_assignments_overlaps(data)
