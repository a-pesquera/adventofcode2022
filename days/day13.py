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


def packet_less_than(packet_1, packet_2):
    for left, right in zip_longest(packet_1, packet_2):
        if left is None:
            # End of packet 1, it's in order
            return True
        if right is None:
            # End of packet 2 before packet 1, it's NOT in order
            return False

        left_is_number = isinstance(left, int)
        right_is_number = isinstance(right, int)
        if left_is_number and right_is_number:
            if left < right:
                return True
            elif left > right:
                return False
            # Not sure... Continue checking
            continue

        left = [left] if left_is_number else left
        right = [right] if right_is_number else right

        result = packet_less_than(left, right)
        if result is not None:
            return result

    # Both packets are the same
    return None


def get_sum_of_indexes_in_right_order(data):
    pair_of_packets = parse_pair_of_packets(data)

    packets_index_start = 1
    ordered_indexes = []
    for i, (packet_1, packet_2) in enumerate(pair_of_packets, packets_index_start):
        if packet_less_than(packet_1, packet_2):
            ordered_indexes.append(i)

    return sum(ordered_indexes)


def quicksort_partition(array, left, right):
    pivot = array[right]
    partition = left - 1

    for i in range(left, right):
        if packet_less_than(array[i], pivot):
            partition += 1
            array[partition], array[i] = array[i], array[partition]

    partition += 1
    array[partition], array[right] = array[right], array[partition]
    return partition


def quicksort(array, left=None, right=None):
    left = left if left is not None else 0
    right = right if right is not None else len(array) - 1

    if left >= right:
        return

    partition = quicksort_partition(array, left, right)
    quicksort(array, left, partition - 1)
    quicksort(array, partition + 1, right)


def multiply_divider_packets_indexes(data):
    pair_of_packets = parse_pair_of_packets(data)
    # Ungroup and put all in a list
    all_packets = [x for pair in pair_of_packets for x in pair]

    # Additional divider packets
    divider_packets = [
        [[2]],
        [[6]],
    ]
    all_packets.extend(divider_packets)

    quicksort(all_packets)

    # Find divider packets in ordered array
    indexes = []
    for divider in divider_packets:
        index = all_packets.index(divider)
        indexes.append(index + 1)

    return indexes[0] * indexes[1]


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return get_sum_of_indexes_in_right_order(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return multiply_divider_packets_indexes(data)
