import common

DATA_FILE = 'day20.txt'
EXAMPLE_FILE = 'day20-example.txt'


def create_list(data):
    return [(i, int(l)) for i, l in enumerate(data)]


def move_turn(lst, index):
    # print('BEFORE', lst)
    value = lst.pop(index)
    original_value = value
    if isinstance(value, tuple):
        value = value[1]

    # print('index', index)
    # print('value', value)
    # print('MIDDLE', lst)

    # Avoid moving multiple times
    move = abs(value) % len(lst)
    # print('move', move)
    if value < 0:
        move *= -1

    new_index = (index + move) % len(lst)
    if new_index == 0:
        # Instead of on the first position, insert at edd
        new_index = len(lst)
    # print('new_index', new_index)

    lst.insert(new_index, original_value)
    # print('AFTER ', lst)
    return lst


def foo(data):
    lst = create_list(data)
    # print('lst', lst)

    for n in range(len(lst)):
        # print('lst', [x[1] for x in lst])
        index = [x[0] for x in lst].index(n)
        # print('Step', n + 1, 'n', n, 'index', index)
        lst = move_turn(lst, index)

    # print('lst', [x[1] for x in lst])

    # Find 0 because it's the "initial" index for coordinates
    initial_coordinate_index = [x[1] for x in lst].index(0)
    coordinate_1_index = (initial_coordinate_index + 1000) % len(lst)
    coordinate_2_index = (initial_coordinate_index + 2000) % len(lst)
    coordinate_3_index = (initial_coordinate_index + 3000) % len(lst)

    return lst[coordinate_1_index][1] + lst[coordinate_2_index][1] + lst[coordinate_3_index][1]


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return foo(data)


def part_2(input_file):
    raise NotImplementedError
