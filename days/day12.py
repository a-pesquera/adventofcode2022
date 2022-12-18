import common

DATA_FILE = 'day12.txt'
EXAMPLE_FILE = 'day12-example.txt'


def create_matrix(data):
    matrix = []
    start = None
    end = None

    unicode_char_integer = ord('a') - 1

    for i, line in enumerate(data):
        row = []
        matrix.append(row)

        for j, lvl in enumerate(line):
            if lvl == 'S':
                lvl = 'a'
                start = (i, j)
            elif lvl == 'E':
                lvl = 'z'
                end = (i, j)

            row.append(ord(lvl) - unicode_char_integer)

    return matrix, start, end


def create_points(point, limits):
    i, j = point
    limit_rows, limit_cols = limits

    option_points = [
        (i - 1, j) if i else None,  # Up
        (i, j + 1) if j < limit_cols - 1 else None,  # Right
        (i + 1, j) if i < limit_rows - 1 else None,  # Down
        (i, j - 1) if j else None,  # Left
    ]
    option_points = [x for x in option_points if x]
    return option_points


def dijkstra_get_smallest(pending_nodes, matrix_distances):
    small_point = None
    small_value = float('Inf')

    for i, j in pending_nodes:
        test_value = matrix_distances[i][j]
        if test_value < small_value:
            small_value = test_value
            small_point = (i, j)

    return small_point


def walk_dijkstra(matrix, start, end_point=None, end_value=None, filter_function=None):
    limits = (len(matrix), len(matrix[0]))

    unvisited_nodes = set((i, j) for i, row in enumerate(matrix) for j, cell in enumerate(row))

    matrix_distances = []
    inf = float('Inf')
    for row in matrix:
        tent_row = []
        for col in row:
            tent_row.append(inf)
        matrix_distances.append(tent_row)

    # Initial point distance is 0
    matrix_distances[start[0]][start[1]] = 0

    pending_nodes = set()
    pending_nodes.add(start)
    while pending_nodes:
        current = dijkstra_get_smallest(pending_nodes, matrix_distances)
        pending_nodes.remove(current)

        option_points = create_points(current, limits)
        option_points = (x for x in option_points if x in unvisited_nodes)

        if filter_function:
            # Part 1: points that are at most 1 value bigger than current
            # Part 2: points that are at lest 1 value lower than current
            option_points = (p for p in option_points if filter_function(matrix, current, p))

        current_distance = matrix_distances[current[0]][current[1]]
        for option_point in option_points:
            option_point_distance = current_distance + 1

            if option_point == end_point:
                return option_point_distance
            elif end_value is not None:
                option_value = matrix[option_point[0]][option_point[1]]
                if option_value == end_value:
                    return option_point_distance

            pending_nodes.add(option_point)

            i, j = option_point
            if matrix_distances[i][j] > option_point_distance:
                matrix_distances[i][j] = option_point_distance

        unvisited_nodes.remove(current)


def walk_bfs(matrix, start, end_point=None, end_value=None, filter_function=None):
    # Breadth-first search
    explored = set()
    queue = []
    limits = (len(matrix), len(matrix[0]))

    # Start point
    queue.append((start, 0))
    explored.add(start)

    while queue:
        current, current_distance = queue.pop(0)

        option_points = create_points(current, limits)
        option_points = (p for p in option_points if p not in explored)

        if filter_function:
            # Part 1: points that are at most 1 value bigger than current
            # Part 2: points that are at lest 1 value lower than current
            option_points = (p for p in option_points if filter_function(matrix, current, p))

        for option_point in option_points:
            option_point_distance = current_distance + 1
            queue.append((option_point, option_point_distance))
            explored.add(option_point)

            if option_point == end_point:
                return option_point_distance
            elif end_value is not None:
                option_value = matrix[option_point[0]][option_point[1]]
                if option_value == end_value:
                    return option_point_distance


def find_fewest_steps(data):
    matrix, start, end = create_matrix(data)
    go_up = lambda matrix, src, dst: matrix[dst[0]][dst[1]] <= matrix[src[0]][src[1]] + 1
    # result = walk_dijkstra(matrix, start, end_point=end, filter_function=go_up)
    result = walk_bfs(matrix, start, end_point=end, filter_function=go_up)
    return result


def find_fewest_steps_until_a(data):
    matrix, _, end = create_matrix(data)
    go_down = lambda matrix, src, dst: matrix[dst[0]][dst[1]] >= matrix[src[0]][src[1]] - 1
    # result = walk_dijkstra(matrix, end, end_value=1, filter_function=go_down)
    result = walk_bfs(matrix, end, end_value=1, filter_function=go_down)
    return result


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return find_fewest_steps(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return find_fewest_steps_until_a(data)
