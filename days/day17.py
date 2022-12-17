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


def play_tetris_with_rocks_and_elephants(data, num_rocks=2022, width=7, generate_y=3, generate_x=2):
    jet_i = 0
    jet_pattern = next(data)
    print('jet_pattern', jet_pattern)

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

    top_height = 0
    # num_rocks = 10  # @TODO delete!!
    for rock_i in range(num_rocks):
        # print('rock_i', rock_i)

        next_rock_x = generate_x
        # print('next_rock_x', next_rock_x)
        next_rock_y = top_height + generate_y
        # print('next_rock_y', next_rock_y)

        rock_bottom_left = (next_rock_x, next_rock_y)
        print('Initial rock_bottom_left', rock_bottom_left)

        # Add new walls
        for n in range(TALLEST_ROCK_HEIGHT):
            # Left wall
            all_boundaries.add((-1, next_rock_y + n))
            # Right wall
            all_boundaries.add((width, next_rock_y + n))

        # @TODO dynamic! Each turn there is a function
        create_rock_fn = ROCKS[rock_i % len(ROCKS)]

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
                print('Movement by jet!', jet_push)
                rock_bottom_left = new_bottom_left
            else:
                print('Collision with walls!')

            # Then, go down
            new_bottom_left = (rock_bottom_left[0], rock_bottom_left[1] - 1)
            # print('new_bottom_left', new_bottom_left)
            rock_after_gravity = create_rock_fn(new_bottom_left)
            # print('rock_after_gravity', rock_after_gravity)

            is_collision = all_boundaries.intersection(rock_after_gravity)
            if not is_collision:
                print('Movement by gravity!')
                rock_bottom_left = new_bottom_left
            else:
                placed_rock_at = rock_bottom_left
                print('Rock placed at:', placed_rock_at)
                break

        placed_rock = create_rock_fn(placed_rock_at)
        print('Full rock:', placed_rock)
        all_boundaries.update(placed_rock)

        # Recalculate height
        placed_rock_height = max([p[1] + 1 for p in placed_rock])
        top_height = max(top_height, placed_rock_height)
        print('new top_height', top_height)

    return top_height


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return play_tetris_with_rocks_and_elephants(data)


def part_2(input_file):
    raise NotImplementedError
