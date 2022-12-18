import common

DATA_FILE = 'day8.txt'
EXAMPLE_FILE = 'day8-example.txt'


def create_matrix(data):
    matrix = []
    for i, line in enumerate(data):
        row_trees = [int(t) for t in line]
        matrix.append(row_trees)
    return matrix


def rotate_matrix(matrix):
    list_of_tuples = zip(*matrix[::-1])
    return [list(elem) for elem in list_of_tuples]


def count_visible_trees(data):
    matrix = create_matrix(data)
    visible_matrix = [list([False] * len(row)) for row in matrix]

    # Find only visible trees IN ROW from left to right
    # Then, rotate both matrix and find trees 3 more times
    # All visible trees are marked in the other matrix
    for _ in range(4):
        matrix = rotate_matrix(matrix)
        visible_matrix = rotate_matrix(visible_matrix)
        for i, row in enumerate(matrix):
            min_height = -1
            for j, col in enumerate(row):
                if col > min_height:
                    min_height = col
                    visible_matrix[i][j] = True

    return sum(1 for row in visible_matrix for cell in row if cell)


def get_best_scenic_score(data):
    matrix = create_matrix(data)
    scenic_score_matrix = [list([1] * len(row)) for row in matrix]

    # Samem as part 1, go only through rows and rotate matrix
    for _ in range(4):
        matrix = rotate_matrix(matrix)
        scenic_score_matrix = rotate_matrix(scenic_score_matrix)

        for i, row in enumerate(matrix[1:-1], 1):  # Ignoring limits
            for j, col in enumerate(row[1:-1], 1):  # Ignoring limits
                count = 0
                tmp_max = -1
                j_start = j + 1

                for j2, col2 in enumerate(row[j_start:], j_start):
                    count += 1
                    if col2 >= col:
                        break
                scenic_score_matrix[i][j] *= count

    return max(col for row in scenic_score_matrix[1:-1] for col in row[1:-1])


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return count_visible_trees(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return get_best_scenic_score(data)
