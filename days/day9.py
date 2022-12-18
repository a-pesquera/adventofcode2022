import common

DATA_FILE = 'day9.txt'
EXAMPLE_FILE = 'day9-example.txt'


def parse_line(line):
    direction, num = line.split(' ')

    directions = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }

    return directions[direction], int(num)


def calculate_tail_movement(head, tail):
    distance = max(abs(head[0] - tail[0]), abs(head[1] - tail[1]))

    if distance <= 1:
        return tail

    delta_x = 0
    if head[0] != tail[0]:
        delta_x = 1 if head[0] > tail[0] else -1

    delta_y = 0
    if head[1] != tail[1]:
        delta_y = 1 if head[1] > tail[1] else -1

    return (tail[0] + delta_x, tail[1] + delta_y)


def count_tail_visited_positions(data, rope_length=2):
    tail_positions = set()

    rope = [(0, 0)] * rope_length

    for line in data:
        direction, num = parse_line(line)

        for _ in range(num):
            # Move head
            head = rope[0]
            rope[0] = (head[0] + direction[0], head[1] + direction[1])

            # Recalculate remaining rope positions
            for i, (pseudo_head, pseudo_tail) in enumerate(zip(rope, rope[1:]), 1):
                rope[i] = calculate_tail_movement(pseudo_head, pseudo_tail)

            tail_positions.add(rope[-1])

    return len(tail_positions)


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return count_tail_visited_positions(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return count_tail_visited_positions(data, rope_length=10)
