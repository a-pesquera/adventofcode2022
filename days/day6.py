import common

DATA_FILE = 'day6.txt'
EXAMPLE_FILE = 'day6-example.txt'


def look_for_marker(text):
    for i, chars in enumerate(zip(text, text[1:], text[2:], text[3:])):
        st = set(chars)
        if len(st) == 4:
            return i + 4


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    line = next(data)
    return look_for_marker(line)


def part_2(input_file):
    raise NotImplementedError
