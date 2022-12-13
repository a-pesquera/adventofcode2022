from itertools import zip_longest

import common

DATA_FILE = 'day13.txt'
EXAMPLE_FILE = 'day13-example.txt'


def parse_pair_of_packets(data):
    pair_of_packets = []

    while True:
        packet_1 = eval(next(data))
        packet_2 = eval(next(data))

        pair_of_packets.append((packet_1, packet_2))

        try:
            # Separation between packets
            _ = next(data)
        except StopIteration:
            break

    return pair_of_packets


def is_in_right_order(packet_1, packet_2):
    # print('is_in_right_order', packet_1, packet_2)
    for a, b in zip_longest(packet_1, packet_2):
        # print('a, b', a, b)

        if a is None:
            return True
        if b is None:
            return False

        a_is_list = isinstance(a, list)
        b_is_list = isinstance(b, list)
        if not a_is_list and not b_is_list:
            if a < b:
                return True
            elif a > b:
                return False
            continue

        a = a if a_is_list else [a]
        b = b if b_is_list else [b]

        partial_result = is_in_right_order(a, b)
        # print('partial_result', partial_result)
        if partial_result is not None:
            return partial_result

    return None


def get_sum_of_indexes_in_right_order(data):
    pair_of_packets = parse_pair_of_packets(data)
    print('pair_of_packets', pair_of_packets)

    ordered_indexes = []

    for i, (packet_1, packet_2) in enumerate(pair_of_packets, 1):
        print('Pair', i)
        print(packet_1, 'vs', packet_2)
        if is_in_right_order(packet_1, packet_2):
            print('Ordered!!')
            ordered_indexes.append(i)
        else:
            print('Not ordered')

    return sum(ordered_indexes)


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return get_sum_of_indexes_in_right_order(data)


def part_2(input_file):
    raise NotImplementedError
