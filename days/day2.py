import common

DATA_FILE = 'day2.txt'
EXAMPLE_FILE = 'day2-example.txt'


def parse_line(line, part=1):
    op, you = line.split(' ')

    ## Alternative form using ABC and XYZ char numbers
    # value_of_opponent = ord(op) - ord('A')
    # if part == 1:
    #     value_of_your_shape = ord(you) - ord('X')
    # elif part == 2:
    #     value_of_your_shape = (value_of_opponent + ord(you) - ord('Y')) % 3
    # return value_of_opponent, value_of_your_shape

    opponent_values = {
        'A': 0,
        'B': 1,
        'C': 2,
    }
    value_of_opponent = opponent_values[op]

    if part == 1:
        your_values = {
            'X': 0,
            'Y': 1,
            'Z': 2,
        }
        value_of_your_shape = your_values[you]
    elif part == 2:
        your_values = {
            # Lose
            'X': (value_of_opponent - 1) % 3,
            # Draw
            'Y': value_of_opponent,
            # Win
            'Z': (value_of_opponent + 1) % 3,
        }
        value_of_your_shape = your_values[you]

    return value_of_opponent, value_of_your_shape


def play_round(opponent, you):
    points = you + 1  # Adding 1 because Rock is 0, Paper 1 and Scissors 2

    # Using modulus we have 0 for tie, 1 for win and 2 (the same as -1) for lose
    play = (you - opponent) % 3
    if play == 0:
        points += 3
    elif play == 1:
        points += 6

    return points


def calculate_points(data, part=1):
    points = 0
    for line in data:
        opponent, you = parse_line(line, part=part)
        points += play_round(opponent, you)
    return points


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return calculate_points(data, part=1)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return calculate_points(data, part=2)
