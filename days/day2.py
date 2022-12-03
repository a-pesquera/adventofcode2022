import common

DATA_FILE = 'day2.txt'
EXAMPLE_FILE = 'day2-example.txt'


def parse_line_part_1(line):
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


def parse_line_part_2(line):
    order = ['Rock', 'Paper', 'Scissors']

    op, you = line.split(' ')

    opponent_values = {
        'A': 0,
        'B': 1,
        'C': 2,
    }
    value_of_opponent = opponent_values[op]

    your_values = {
        # Lose
        'X': (value_of_opponent - 1) % 3,
        # Draw
        'Y': value_of_opponent,
        # Win
        'Z': (value_of_opponent + 1) % 3,
    }
    value_of_your_shape = your_values[you]

    return (order[value_of_opponent], order[value_of_your_shape])


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


def calculate_points_part_1(data):
    points = 0
    for line in data:
        opponent, you = parse_line_part_1(line)
        points += play_round(opponent, you)
    return points


def calculate_points_part_2(data):
    points = 0
    for line in data:
        opponent, you = parse_line_part_2(line)
        points += play_round(opponent, you)
    return points


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return calculate_points_part_1(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return calculate_points_part_2(data)
