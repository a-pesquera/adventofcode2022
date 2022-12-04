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


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return count_assignments_fully_contains(data)


def part_2(input_file):
    raise NotImplementedError
