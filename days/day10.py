import common

DATA_FILE = 'day10.txt'
EXAMPLE_FILE = 'day10-example.txt'


def do_cpu(data, cycle_offset=20, cycle_freq=40, crt_row=40):
    cycle = 0
    registry_x = 1

    signals = []
    crt = ''

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

            # Render CRT
            is_pixel_light = registry_x - 1 <= (cycle - 1) % crt_row <= registry_x + 1
            crt += '#' if is_pixel_light else '.'

            # End of cycle
            if op[0] == 'addx':
                registry_x += op[1]

    chunks = []
    while crt:
        chunk = crt[:crt_row]
        crt = crt[crt_row:]
        chunks.append(chunk)
    return sum(signals), chunks


def sum_of_signals(data, cycle_offset=20, cycle_freq=40):
    sum_signals, _ = do_cpu(data, cycle_offset=cycle_offset, cycle_freq=cycle_freq)
    return sum_signals


def crt_output(data, crt_row=40):
    _, crt_output = do_cpu(data, crt_row=crt_row)
    return crt_output


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return sum_of_signals(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return crt_output(data)
