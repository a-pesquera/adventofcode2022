from collections import deque
import re

import common

DATA_FILE = 'day19.txt'
EXAMPLE_FILE = 'day19-example.txt'

PARSE_RE = re.compile(r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')

BUILD_OPTIONS = ['ORE', 'CLAY', 'OBSIDIAN', 'GEODE']


def create_options(resources, robots, factory_costs, time_remaining):
    options = ['NOTHING']

    max_ore_robots = max(x[0] for x in factory_costs)
    max_clay_robots = factory_costs[2][1]
    max_obsidian_robots = factory_costs[3][2]
    max_robots_cost = [
        max(x[0] for x in factory_costs),
        max_clay_robots,
        max_obsidian_robots,
    ]

    for i, factory_cost in enumerate(factory_costs):
        if i <= 2:
            if robots[i] >= max_robots_cost[i]:
                continue
            elif time_remaining * robots[i] + resources[i] >= time_remaining * max_robots_cost[i]:
                continue

        if resources[0] >= factory_cost[0] and resources[1] >= factory_cost[1] and resources[2] >= factory_cost[2]:
            # options.append(BUILD_OPTIONS[i])
            options.append(i)

    return options


def get_max_geodes(ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian, minutes):
    resources = [0, 0, 0, 0]
    robots = [1, 0, 0, 0]
    factory_costs = [
        [ore_ore, 0, 0],
        [clay_ore, 0, 0],
        [obsidian_ore, obsidian_clay, 0],
        [geode_ore, 0, geode_obsidian],
    ]

    stack = deque()

    minute = 0
    initial_state = (minute, tuple(resources), tuple(robots))
    stack.append(initial_state)

    discovered = set()

    max_geodes = 0

    while stack:
        state = stack.pop()
        if state not in discovered:
            discovered.add(state)

            minute, resources, robots = state
            # print('minute', minute, 'resources', resources, 'robots', robots)

            if minute == minutes:
                max_geodes = max(max_geodes, resources[-1])
                continue

            next_minute = minute + 1
            next_resources = (resources[0] + robots[0], resources[1] + robots[1], resources[2] + robots[2], resources[3] + robots[3])

            options = create_options(resources, robots, factory_costs, minutes - next_minute)
            for option in options:
                # print('option', option)

                option_minute = next_minute

                option_resources = next_resources

                option_robots = robots
                if option != 'NOTHING':
                    idx = option
                    # idx = BUILD_OPTIONS.index(option)

                    option_robots = list(option_robots)
                    option_robots[idx] += 1
                    option_robots = tuple(option_robots)

                    costs = factory_costs[idx]
                    option_resources = (option_resources[0] - costs[0], option_resources[1] - costs[1], option_resources[2] - costs[2], option_resources[3])

                option_state = (minute + 1, option_resources, option_robots)
                stack.append(option_state)

    return max_geodes


def foo(data):
    minutes = 24

    quality_levels = []

    for line in data:
        tpl = tuple(int(x) for x in PARSE_RE.match(line).groups())
        bp_id, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = tpl
        print(line)
        print('Doing BP', bp_id)
        max_geodes = get_max_geodes(ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian, minutes)
        print('max_geodes', max_geodes)
        quality_level = bp_id * max_geodes
        quality_levels.append(quality_level)
        print('quality_level', quality_level, flush=True)

    return sum(quality_levels)


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return foo(data)


def part_2(input_file):
    raise NotImplementedError
