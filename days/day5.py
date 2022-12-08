import re

import common

DATA_FILE = 'day5.txt'
EXAMPLE_FILE = 'day5-example.txt'

STEP_RE = re.compile(r'move (\d+) from (\d+) to (\d+)')


def parse_stacks(lines):
    stacks = []
    for line in lines:
        for i, crate in enumerate(line[1::4]):
            if len(stacks) <= i:
                stacks.append([])
            if crate != ' ':
                stacks[i].insert(0, crate)
    return stacks


def parse_step(line):
    num, src, dest = tuple(int(x) for x in STEP_RE.match(line).groups())
    return num, src, dest


def get_end_crates(data, part=1):
    stacks_lines = []
    for line in data:
        if line == '\n':
            break
        stacks_lines.append(line)

    # Ignore line with stacks numbers: " 1   2   3..."
    stacks_lines.pop()

    stacks = parse_stacks(stacks_lines)

    for line in data:
        num, src, dest = parse_step(line)
        # Pick crates "num" times
        tmp_stack = stacks[src - 1][-1 * num:]
        stacks[src - 1] = stacks[src - 1][:-1 * num]
        if part == 1:
            # Place them in reversed
            stacks[dest - 1].extend(reversed(tmp_stack))
        elif part == 2:
            # Place them in block
            stacks[dest - 1].extend(tmp_stack)

    result = ''
    for stack in stacks:
        result += stack.pop()

    return result


def part_1(input_file):
    data = common.read_data_file_generator(input_file, strip=False)
    return get_end_crates(data, part=1)


def part_2(input_file):
    data = common.read_data_file_generator(input_file, strip=False)
    return get_end_crates(data, part=2)
