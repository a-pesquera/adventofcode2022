import common

DATA_FILE = 'day10.txt'
EXAMPLE_FILE = 'day10-example.txt'


CRT_ROW = 40
REGISTRY_X_INITIAL = 1
CYCLE_OFFSET = 20
CYCLE_FREQUENCY = 40


def do_cycle(cycle, registry_x, signals):
    # Start of cycle
    cycle += 1
    if (cycle - CYCLE_OFFSET) % CYCLE_FREQUENCY == 0:
        signals.append(cycle * registry_x)

    # Render pixel
    is_pixel_light = registry_x - 1 <= (cycle - 1) % CRT_ROW <= registry_x + 1
    pixel = '#' if is_pixel_light else '.'

    return cycle, pixel


def create_chunks(s, size):
    chunks = []
    while s:
        chunks.append(s[:size])
        s = s[size:]
    return chunks


def do_cpu(data):
    cycle = 0
    registry_x = REGISTRY_X_INITIAL
    signals = []
    crt = ''

    for line in data:
        cycle, pixel = do_cycle(cycle, registry_x, signals)
        crt += pixel

        if line != 'noop':
            cycle, pixel = do_cycle(cycle, registry_x, signals)
            crt += pixel
            registry_x += int(line.split(' ')[-1])

    return sum(signals), create_chunks(crt, CRT_ROW)


def sum_of_signals(data):
    sum_signals, _ = do_cpu(data)
    return sum_signals


def crt_output(data):
    _, crt_output = do_cpu(data)
    return crt_output


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return sum_of_signals(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return crt_output(data)
