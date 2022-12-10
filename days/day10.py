import common

DATA_FILE = 'day10.txt'
EXAMPLE_FILE = 'day10-example.txt'


def sum_of_signals(data, cycle_offset=20, cycle_freq=40):
    cycle = 0
    registry_x = 1

    signals = []

    for line in data:
        operations = []

        if line == 'noop':
            operations.append(('sleep',))
        else:
            operations.extend([
                ('sleep',),
                ('addx', int(line.split(' ')[-1]))
            ])

        for op in operations:
            cycle += 1

            # Start of cycle
            if (cycle - cycle_offset) % cycle_freq == 0:
                signals.append(cycle * registry_x)

            # End of cycle
            if op[0] == 'addx':
                registry_x += op[1]

    return sum(signals)


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return sum_of_signals(data)


def part_2(input_file):
    raise NotImplementedError
