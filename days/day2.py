import common

DATA_FILE = 'day2.txt'
EXAMPLE_FILE = 'day2-example.txt'


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


def parse_line(line):
    op, you = line.split(' ')
    values = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
        'X': 'Rock',
        'Y': 'Paper',
        'Z': 'Scissors',
    }
    return (values[op], values[you])


def play_round(opponent, you):
    points = 0

    selected_shape = {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3,
    }
    points += selected_shape[you]

    if opponent == you:
        points += 3
    elif opponent == 'Rock' and you == 'Paper':
        points += 6
    elif opponent == 'Paper' and you == 'Scissors':
        points += 6
    elif opponent == 'Scissors' and you == 'Rock':
        points += 6

    return points


def calculate_points(data):
    points = 0
    for line in data:
        opponent, you = parse_line(line)
        points += play_round(opponent, you)
    return points


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return calculate_points(data)


def part_2(input_file):
    raise NotImplementedError
