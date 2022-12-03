
import common


def function(data):
    elfs = []
    current = 0
    for l in data:
        if l == '':
            elfs.append(current)
            current = 0
        else:
            current += int(l)

    # Handle last line not being a new line
    if current:
        elfs.append(current)

    return max(elfs)


def part1(input_file):
    data = common.read_data_file_generator(input_file)
    return function(data)
