
import common


def elfs_weights(data):
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
    return elfs


def elf_with_max_weight(data):
    elfs = elfs_weights(data)
    return max(elfs)


def top_3_elfs_with_max_weight(data):
    elfs = elfs_weights(data)
    elfs.sort(reverse=True)
    return sum(elfs[:3])


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return elf_with_max_weight(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return top_3_elfs_with_max_weight(data)
