import common

DATA_FILE = 'day8.txt'
EXAMPLE_FILE = 'day8-example.txt'


def is_hidden(matrix, row, column):
    row_trees = matrix[row]
    actual_tree = row_trees[column]

    # First, check row
    # Check left part
    for tree in row_trees[:column]:
        if tree >= actual_tree:
            break
    else:
        return False

    # Check right part
    for tree in row_trees[column + 1:]:
        if tree >= actual_tree:
            break
    else:
        return False

    # Second, check column
    # Check top part
    for i in range(0, row):
        tree = matrix[i][column]
        if tree >= actual_tree:
            break
    else:
        return False

    # Check bottom part
    for i in range(row + 1, len(matrix)):
        tree = matrix[i][column]
        if tree >= actual_tree:
            break
    else:
        return False

    return True


def create_matrix(data):
    matrix = []
    for i, line in enumerate(data):
        row_trees = [int(t) for t in line]
        matrix.append(row_trees)
    return matrix


def count_visible_trees(data):
    matrix = create_matrix(data)

    # print('Forest')
    # for row in matrix:
    #     print(row)

    edge_count = (len(matrix) * 2) + ((len(matrix[0]) - 2) * 2)

    count = 0

    for i, row in enumerate(matrix[1:-1], 1):
        for j, col in enumerate(row[1:-1], 1):
            is_hid = is_hidden(matrix, i, j)
            if not is_hid:
                count += 1

    return edge_count + count


def calculate_score(matrix, row, column):
    row_trees = matrix[row]
    actual_tree = row_trees[column]

    # First, check row
    # Check left part
    left_count = 0
    for tree in reversed(row_trees[:column]):
        left_count += 1
        if tree >= actual_tree:
            break
    # print('left_count', left_count)

    # Check right part
    right_count = 0
    for tree in row_trees[column + 1:]:
        right_count += 1
        if tree >= actual_tree:
            break
    # print('right_count', right_count)

    # Second, check column
    # Check top part
    top_count = 0
    for i in reversed(range(0, row)):
        tree = matrix[i][column]
        top_count += 1
        if tree >= actual_tree:
            break
    # print('top_count', top_count)

    # Check bottom part
    bottom_count = 0
    for i in range(row + 1, len(matrix)):
        tree = matrix[i][column]
        bottom_count += 1
        if tree >= actual_tree:
            break
    # print('bottom_count', top_count)

    # print(left_count, right_count, top_count, bottom_count)

    return left_count * right_count * top_count * bottom_count


def get_best_scenic_score(data):
    matrix = create_matrix(data)

    # print('Forest')
    # for row in matrix:
    #     print(row)

    max_score = 0

    for i, row in enumerate(matrix[1:-1], 1):
        for j, col in enumerate(row[1:-1], 1):
            score = calculate_score(matrix, i, j)
            # print('Score', (i, j), score)
            if score > max_score:
                max_score = score

    return max_score


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return count_visible_trees(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return get_best_scenic_score(data)
