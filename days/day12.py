import common

DATA_FILE = 'day12.txt'
EXAMPLE_FILE = 'day12-example.txt'


# # is block (value 0)
# S is start (value 1)
# E is end (max value)
ELEVATIONS = '#SabcdefghijklmnopqrstuvwxyzE'


def create_matrix(data):
    matrix = []
    for i, line in enumerate(data):
        row_trees = [ELEVATIONS.index(t) for t in line]
        matrix.append(row_trees)
    return matrix


def print_matrix(matrix, raw=False, pointer=None, blocked_points=None):
    if blocked_points is None:
        blocked_points = set()

    block_char = '.'

    print(block_char * (len(matrix[0]) + 2))
    for i, row in enumerate(matrix):
        print(block_char, end='')
        for j, cell in enumerate(row):
            if (i, j) == pointer:
                print('@', end='')
            elif (i, j) in blocked_points:
                print(ELEVATIONS[0], end='')
            elif raw:
                print(cell, end='')
            else:
                print(ELEVATIONS[cell], end='')
        print(block_char)
    print(block_char * (len(matrix[0]) + 2))


def print_matrix_2(matrix):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            print(cell, end=', ')
        print()


def find_start_and_end(matrix):
    start = None
    end = None

    value_start = ELEVATIONS.index('S')
    value_end = ELEVATIONS.index('E')

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == value_start:
                start = (i, j)
                if end:
                    return start, end
            elif cell == value_end:
                end = (i, j)
                if start:
                    return start, end
    raise NotImplementedError


def walk_v1(matrix, point, end, blocked_points=None, depth=1):
    # print('=' * 40)
    # print('Start of walk - depth', depth)
    if blocked_points is None:
        blocked_points = set()
    else:
        new_blocked_points = blocked_points.copy()
        blocked_points = new_blocked_points

    # print_matrix(matrix, pointer=point, blocked_points=blocked_points)

    blocked_points.add(point)

    if point == end:
        # print('iosafonsadionas', new_blocked_points)
        # print('iosafonsadionas', len(new_blocked_points) - 1)
        return len(new_blocked_points) - 1

    limit_rows = len(matrix)
    limit_cols = len(matrix[0])

    i, j = point
    actual = matrix[i][j]
    # print(f'Actual: {ELEVATIONS[actual]} (num {actual} on point {point})')

    option_points = [
        (i - 1, j) if i else None,  # Up
        (i, j + 1) if j < limit_cols - 1 else None,  # Right
        (i + 1, j) if i < limit_rows - 1 else None,  # Down
        (i, j - 1) if j else None,  # Left
    ]
    option_points = [x for x in option_points if x and x not in blocked_points]

    # print('option_points', option_points)

    # First, try to go up
    for option_point in option_points:
        # print('option_point', option_point)
        oi, oj = option_point
        option_actual = matrix[oi][oj]
        if actual + 1 == option_actual:
            # print('Yay!')
            # print(f'Option actual: {ELEVATIONS[option_actual]} (num {option_actual} on point {option_point})')
            result = walk(matrix, option_point, end, blocked_points, depth=depth + 1)
            if result:
                return result
    # Then, try to go on the same level
    for option_point in option_points:
        # print('option_point', option_point)
        oi, oj = option_point
        option_actual = matrix[oi][oj]
        if actual == option_actual:
            # print('Meh')
            # print(f'Option actual: {ELEVATIONS[option_actual]} (num {option_actual} on point {option_point})')
            result = walk(matrix, option_point, end, blocked_points, depth=depth + 1)
            if result:
                return result

    # print('Going back...')
    return None


def walk_dijkstra(matrix, start, end):
    limit_rows = len(matrix)
    limit_cols = len(matrix[0])

    unvisited_set = set((i, j) for i, row in enumerate(matrix) for j, cell in enumerate(row))

    matrix_distances = []
    for row in matrix:
        tent_row = []
        for col in row:
            tent_row.append(1e20)
        matrix_distances.append(tent_row)

    matrix_distances[start[0]][start[1]] = 0

    # print_matrix(matrix)
    # print_matrix_2(matrix_distances)

    with_value = set()
    with_value.add(start)

    def get_smallest(with_value, matrix_distances):
        lst = list(with_value)
        small_point = lst.pop()
        small_value = matrix_distances[small_point[0]][small_point[1]]
        for i, j in lst:
            test_value = matrix_distances[i][j]
            if test_value < small_value:
                small_point = (i, j)
        with_value.remove(small_point)
        return small_point

    while with_value:
        current = get_smallest(with_value, matrix_distances)
        i, j = current
        current_distance = matrix_distances[i][j]
        if current == end:
            break

        option_points = [
            (i - 1, j) if i else None,  # Up
            (i, j + 1) if j < limit_cols - 1 else None,  # Right
            (i + 1, j) if i < limit_rows - 1 else None,  # Down
            (i, j - 1) if j else None,  # Left
        ]
        option_points = [x for x in option_points if x and x in unvisited_set]
        option_points = [x for x in option_points if matrix[x[0]][x[1]] <= matrix[i][j] + 1]
        # print('option_points', option_points)
        for option_point in option_points:
            with_value.add(option_point)
            oi, oj = option_point
            # print('option_point', option_point)
            tentative_distance = current_distance + 1
            # print('tentative_distance', tentative_distance)
            if matrix_distances[oi][oj] > tentative_distance:
                matrix_distances[oi][oj] = tentative_distance
        unvisited_set.remove(current)

        # print_matrix_2(matrix_distances)
        # break
    print_matrix_2(matrix_distances)
    return current_distance


def walk(matrix, start, end):
    # Breadth-first_search
    limit_rows = len(matrix)
    limit_cols = len(matrix[0])

    matrix[end[0]][end[1]] -= 1

    explored = set()
    explored.add(start)

    queue = []
    queue.append((start, 0))

    while queue:
        current, current_distance = queue.pop(0)

        i, j = current

        option_points = [
            (i - 1, j) if i else None,  # Up
            (i, j + 1) if j < limit_cols - 1 else None,  # Right
            (i + 1, j) if i < limit_rows - 1 else None,  # Down
            (i, j - 1) if j else None,  # Left
        ]
        option_points = [x for x in option_points if x and x not in explored]
        option_points = [x for x in option_points if matrix[x[0]][x[1]] <= matrix[i][j] + 1]

        for option_point in option_points:
            queue.append((option_point, current_distance + 1))
            explored.add(option_point)

            if option_point == end:
                return current_distance + 1

    return current_distance


def find_fewest_steps(data):
    matrix = create_matrix(data)
    start, end = find_start_and_end(matrix)
    result = walk(matrix, start, end)
    return result


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return find_fewest_steps(data)


def part_2(input_file):
    raise NotImplementedError
