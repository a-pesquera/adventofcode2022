import common

DATA_FILE = 'day17.txt'
EXAMPLE_FILE = 'day17-example.txt'


ROCKS = [
    lambda p: set((p[0] + dx, p[1]) for dx in range(4)),
    lambda p: {(p[0] + 1, p[1] + 1), (p[0] + 1, p[1] + 2), (p[0] + 1, p[1]), (p[0], p[1] + 1), (p[0] + 2, p[1] + 1)},
    lambda p: set((p[0] + dx, p[1]) for dx in range(3)) | set((p[0] + 2, p[1] + 1 + dy) for dy in range(2)),
    lambda p: set((p[0], p[1] + dy) for dy in range(4)),
    lambda p: set(((p[0] + dx, p[1] + dy)) for dx in range(2) for dy in range(2)),
]
TALLEST_ROCK_HEIGHT = 4


def render(boundaries, width):
    only_rocks = set(b for b in boundaries if b[0] != -1 and b[0] != width and b[1] != -1)
    max_height = 0
    if only_rocks:
        max_height = max(r[1] for r in only_rocks) + 1

    for h in reversed(range(max_height)):
        for w in range(width):
            point = (w, h)
            char = '.'
            if point in only_rocks:
                char = '#'
            print(char, end='')
        print()


def play_game(num_rocks, jet_pattern, search_for_monolith=False, width=7, generate_y=3, generate_x=2):
    rocks_codex = {}
    rocks_history = []

    all_boundaries = set()
    # Floor
    for n in range(width):
        all_boundaries.add((n, -1))
    # Initial walls
    for n in range(generate_y):
        # Left wall
        all_boundaries.add((-1, n))
        # Right wall
        all_boundaries.add((width, n))
    # print('all_boundaries', all_boundaries)

    jet_i = 0
    top_height = 0
    for rock_i in range(num_rocks):
        # print('rock_i', rock_i)
        rock_type = rock_i % len(ROCKS)

        next_rock_x = generate_x
        # print('next_rock_x', next_rock_x)
        next_rock_y = top_height + generate_y
        # print('next_rock_y', next_rock_y)

        rock_bottom_left = (next_rock_x, next_rock_y)
        # print('Initial rock_bottom_left', rock_bottom_left)

        # Add new walls
        for n in range(TALLEST_ROCK_HEIGHT):
            # Left wall
            all_boundaries.add((-1, next_rock_y + n))
            # Right wall
            all_boundaries.add((width, next_rock_y + n))

        # @TODO dynamic! Each turn there is a function
        create_rock_fn = ROCKS[rock_type]

        placed_rock_at = None
        while True:
            # First, jet movement
            jet_push = jet_pattern[jet_i % len(jet_pattern)]
            jet_i += 1
            delta_x = 1 if jet_push == '>' else -1

            new_bottom_left = (rock_bottom_left[0] + delta_x, rock_bottom_left[1])
            # print('new_bottom_left', new_bottom_left)
            rock_after_jet = create_rock_fn(new_bottom_left)
            # print('rock_after_jet', rock_after_jet)

            is_collision = all_boundaries.intersection(rock_after_jet)
            if not is_collision:
                # print('Movement by jet!', jet_push)
                rock_bottom_left = new_bottom_left
            else:
                pass
                # print('Collision with walls!')

            # Then, go down
            new_bottom_left = (rock_bottom_left[0], rock_bottom_left[1] - 1)
            # print('new_bottom_left', new_bottom_left)
            rock_after_gravity = create_rock_fn(new_bottom_left)
            # print('rock_after_gravity', rock_after_gravity)

            is_collision = all_boundaries.intersection(rock_after_gravity)
            if not is_collision:
                # print('Movement by gravity!')
                rock_bottom_left = new_bottom_left
            else:
                placed_rock_at = rock_bottom_left
                # print('Rock placed at:', placed_rock_at)
                break

        # print('placed_rock_at', placed_rock_at)
        placed_rock = create_rock_fn(placed_rock_at)
        # print('Full rock:', placed_rock)
        all_boundaries.update(placed_rock)

        # Recalculate height
        placed_rock_height = max([p[1] + 1 for p in placed_rock])
        top_height = max(top_height, placed_rock_height)
        # print('new top_height', top_height)

        if not search_for_monolith:
            continue

        # Register rock
        x_value = placed_rock_at[0]
        key = (rock_type, x_value)
        if key not in rocks_codex:
            rocks_codex[key] = []
        rocks_history.append(key)
        rocks_codex[key].append(rock_i)

        # print('=' * 60)
        # print('rocks_codex', rocks_codex)
        # print('rocks_history', rocks_history)
        # render(all_boundaries, width)

        for a in rocks_codex[key][:-1]:
            # print('a', a)
            monolith_size = rock_i - a
            if monolith_size < 3:
                continue
            # print('possible monolith of size', monolith_size)

            for n in range(monolith_size):
                compare_b = len(rocks_history) - 1 - n
                compare_a = compare_b - monolith_size
                # print('n', n)
                # print('compare_a', compare_a, rocks_history[compare_a])
                # print('compare_b', compare_b, rocks_history[compare_b])
                if compare_a < 0:
                    break
                if rocks_history[compare_a] != rocks_history[compare_b]:
                    break
            else:
                render(all_boundaries, width)
                print('>' * 30, 'Monolith found!!!!!!')
                print('monolith_size', monolith_size)
                print('last from monolith', key)
                print('first from monolith', rocks_history[-monolith_size])

                monolith_repeated_to = len(rocks_history) - 1
                monolith_repeated_from = monolith_repeated_to - monolith_size + 1
                monolith_original_to = monolith_repeated_from - 1
                monolith_original_from = monolith_original_to - monolith_size + 1
                print(f'2nd monolith position:', monolith_repeated_from, monolith_repeated_to)
                print(f'1st monolith position:', monolith_original_from, monolith_original_to)

                return {
                    'size': monolith_size,
                    'offset': monolith_original_from + 1,
                }

    # print('=' * 80)
    # render(all_boundaries, width)

    return top_height


def play_tetris_with_rocks_and_elephants(data, num_rocks=2022):
    jet_pattern = next(data)
    # print('jet_pattern', jet_pattern)

    top_height = play_game(num_rocks, jet_pattern)

    return top_height


def play_tetris_with_rocks_and_elephants_part_2(data, num_rocks=2022):
    jet_pattern = next(data)
    # print('jet_pattern', jet_pattern)

    monolith_data = play_game(num_rocks, jet_pattern, search_for_monolith=True)


    before_monolith_num_rocks = monolith_data['offset'] - 1
    before_monolith_height = play_game(before_monolith_num_rocks, jet_pattern)

    with_1_monolith_height = play_game(before_monolith_num_rocks + monolith_data['size'], jet_pattern)

    print('monolith_data', monolith_data)
    monolith_height = with_1_monolith_height - before_monolith_height
    print('before_monolith_height', before_monolith_height)
    print('monolith_height', monolith_height)

    monolith_filled_num_rocks = num_rocks - before_monolith_num_rocks
    num_monoliths = monolith_filled_num_rocks // monolith_data['size']
    partial_monolith_num_rocks = monolith_filled_num_rocks % monolith_data['size']
    print('monolith_filled_num_rocks', num_monoliths, partial_monolith_num_rocks)

    height_without_monoliths = play_game(before_monolith_num_rocks + partial_monolith_num_rocks, jet_pattern)

    return height_without_monoliths + num_monoliths * monolith_height


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return play_tetris_with_rocks_and_elephants(data)


def part_2(input_file, num_rocks=1_000_000_000_000):
    data = common.read_data_file_generator(input_file)
    return play_tetris_with_rocks_and_elephants_part_2(data, num_rocks=num_rocks)
