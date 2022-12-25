from collections import deque
import re

import common

DATA_FILE = 'day19.txt'
EXAMPLE_FILE = 'day19-example.txt'

PARSE_RE = re.compile(r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')


def can_create_robot(i, resources, factory_cost):
    if resources[0] >= factory_cost[i][0] and resources[1] >= factory_cost[i][1] and resources[2] >= factory_cost[i][2]:
        return True
    return False


def should_create_robot(i, resources, factory_costs, robots, max_robots_cost, remaining_minutes):
    if i == 3:  # Geode robot, always
        return True

    if remaining_minutes * robots[i] + resources[i] >= remaining_minutes * max_robots_cost[i]:
        return False
    return True


def get_max_geodes(ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian, minutes):
    resources = (0, 0, 0, 0)
    robots = (1, 0, 0, 0)
    factory_costs = [
        (ore_ore, 0, 0),
        (clay_ore, 0, 0),
        (obsidian_ore, obsidian_clay, 0),
        (geode_ore, 0, geode_obsidian),
    ]

    max_ore_robots = max(x[0] for x in factory_costs)
    max_clay_robots = factory_costs[2][1]
    max_obsidian_robots = factory_costs[3][2]
    max_robots_cost = [
        max(x[0] for x in factory_costs[1:]),  # Ignore ore robots
        max_clay_robots,
        max_obsidian_robots,
        float('Inf'),
    ]
    priority = list(reversed(range(len(robots))))

    stack = deque()

    minute = 1
    created_robots_history = tuple()
    initial_state = (minute, tuple(resources), tuple(robots), created_robots_history)
    stack.append(initial_state)

    discovered = set()

    max_geodes = 0

    while stack:
        state = stack.pop()
        if state not in discovered:
            discovered.add(state)
            minute, resources, robots, history = state
            # print('minute', minute, 'resources', resources, 'robots', robots, 'history', history)

            remaining_minutes = minutes - minute + 1
            estimate_geodes_production = resources[-1] + robots[-1] * remaining_minutes
            estimate_factory_production = (remaining_minutes * (remaining_minutes + 1)) // 2
            if estimate_geodes_production + estimate_factory_production < max_geodes:
                continue

            # Create states for factory
            if minute < minutes:
                for idx in priority:
                    if robots[idx] >= max_robots_cost[idx]:
                        continue

                    infinite_resources = all(resources[j] - robots[j] >= cost for j, cost in enumerate(factory_costs[idx]))
                    previous_skipped = not history or (history[-1][0] < minute - 1)
                    if infinite_resources and previous_skipped:
                        continue

                    if not can_create_robot(idx, resources, factory_costs):
                        continue
                    if not should_create_robot(idx, resources, factory_costs, robots, max_robots_cost, remaining_minutes):
                        continue

                    new_robots = list(robots)
                    new_robots[idx] += 1
                    new_robots = tuple(new_robots)

                    # Harvest before creating a robo
                    new_resources = (resources[0] + robots[0], resources[1] + robots[1], resources[2] + robots[2], resources[3] + robots[3])

                    costs = factory_costs[idx]
                    new_resources = (new_resources[0] - costs[0], new_resources[1] - costs[1], new_resources[2] - costs[2], new_resources[3])

                    new_history = list(history)
                    new_history.append((minute, idx))
                    new_history = tuple(new_history)

                    factory_state = (minute + 1, new_resources, new_robots, new_history)
                    stack.append(factory_state)

            # Harvest
            resources = (resources[0] + robots[0], resources[1] + robots[1], resources[2] + robots[2], resources[3] + robots[3])

            if minute == minutes:
                max_geodes = max(max_geodes, resources[-1])
                continue

            do_nothing_state = (minute + 1, resources, robots, history)
            stack.append(do_nothing_state)

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
