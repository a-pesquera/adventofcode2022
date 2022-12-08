
import common


def elfs_weights(data):
    elfs = [0]
    for l in data:
        if l == '':
            elfs.append(0)
        else:
            elfs[-1] += int(l)
    return elfs


def elf_with_max_weight(data):
    elfs = elfs_weights(data)
    return max(elfs)


def top_3_elfs_with_max_weight(data):
    elfs = elfs_weights(data)
    elfs.sort()
    return sum(elfs[-3:])


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return elf_with_max_weight(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return top_3_elfs_with_max_weight(data)
