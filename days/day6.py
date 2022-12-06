import common

DATA_FILE = 'day6.txt'
EXAMPLE_FILE = 'day6-example.txt'


def look_for_marker(text, num=4):
    lsts = []
    for n in range(num):
        lsts.append(text[n:])

    for i, chars in enumerate(zip(*lsts)):
        st = set(chars)
        if len(st) == num:
            return i + num


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    line = next(data)
    return look_for_marker(line)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    line = next(data)
    return look_for_marker(line, num=14)
