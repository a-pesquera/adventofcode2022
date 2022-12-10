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

    new_tail = None

    if head[0] == tail[0]:
        # vertical
        new_tail = (tail[0], (head[1] + tail[1]) // 2)
    elif head[1] == tail[1]:
        # horizontal
        new_tail = ((head[0] + tail[0]) // 2, tail[1])
    else:
        # diagonal
        new_tail_x = None
        new_tail_y = None
        if head[0] > tail[0]:
            new_tail_x = tail[0] + 1
        else:
            new_tail_x = tail[0] - 1
        if head[1] > tail[1]:
            new_tail_y = tail[1] + 1
        else:
            new_tail_y = tail[1] - 1
        new_tail = (new_tail_x, new_tail_y)

    return new_tail


def count_tail_visited_positions(data, rope_length=2):
    tail_positions = set()

    rope = [(0, 0)] * rope_length
    tail_positions.add(rope[-1])

    for line in data:
        direction, num = parse_line(line)
        for x in range(num):
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
