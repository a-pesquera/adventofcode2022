import re

import common

DATA_FILE = 'day5.txt'
EXAMPLE_FILE = 'day5-example.txt'

STEP_RE = re.compile(r'move (\d+) from (\d+) to (\d+)')


def parse_stacks(lines):
    stacks = []
    for line in lines:
        stack_idx = 0
        while line:
            crate = line[0:4].strip()
            line = line[4:]

            if len(stacks) < stack_idx + 1:
                stacks.append([])

            if crate:
                stacks[stack_idx].insert(0, crate[1])

            stack_idx += 1
    return stacks


def parse_step(line):
    num, from_, to = (int(x) for x in STEP_RE.match(line).groups())
    return [(from_, to)] * num


def do_step(stacks, step):
    from_, to = (x - 1 for x in step)
    crate = stacks[from_].pop()
    stacks[to].append(crate)
    return stacks


def get_end_crates(data):
    stacks_lines = []
    for line in data:
        line = line.rstrip()
        if line.startswith(' 1   2'):
            # Ignore next empty line
            next(data)
            break
        stacks_lines.append(line.rstrip())

    stacks = parse_stacks(stacks_lines)

    steps = []
    for line in data:
        line_steps = parse_step(line.strip())
        for line_step in line_steps:
            last = steps[-1] if steps else None
            if last and last[0] == line_step[1] and last[1] == line_step[0]:
                steps.pop()
            else:
                steps.append(line_step)

    for step in steps:
        stacks = do_step(stacks, step)

    result = ''
    for stack in stacks:
        result += stack.pop()

    return result



def part_1(input_file):
    data = common.read_data_file_generator(input_file, strip=False)
    return get_end_crates(data)


def part_2(input_file):
    raise NotImplementedError