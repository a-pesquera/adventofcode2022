import re

import common

DATA_FILE = 'day7.txt'
EXAMPLE_FILE = 'day7-example.txt'

STEP_RE = re.compile(r'^(\d+) (.+)$')


def create_tree(data):
    first_line = next(data)
    if first_line != '$ cd /':
        raise Exception('Unexpected initial line')

    subpaths = []
    root = {}
    actual = root

    for line in data:
        if line == '$ cd ..':
            # Go 1 down
            actual = subpaths.pop() if subpaths else root
        elif line.startswith('$ cd '):
            # Go 1 up
            subpaths.append(actual)

            name = line[5:]
            if name not in actual:
                actual[name] = {}
            actual = actual[name]
        elif line == '$ ls' or line.startswith('dir '):
            # Irrelevant
            pass
        else:
            # Is "ls" output for files
            size, name = STEP_RE.match(line).groups()
            actual[name] = int(size)
    return root


def calculate_folder_size(node):
    if not isinstance(node, dict):
        # This is a file
        return node

    size = 0
    for content in node.values():
        size += calculate_folder_size(content)
    return size


def find_top_sizes(node, top_limit):
    accumulated_size = 0

    # Add folder to accumulated
    folder_size = calculate_folder_size(node)
    if folder_size <= top_limit:
        accumulated_size += folder_size

    # Add subfolders to accumulated
    for content in node.values():
        if not isinstance(content, dict):
            continue
        accumulated_size += find_top_sizes(content, top_limit)

    return accumulated_size


def find_top_directory(node, required_limit):
    result = None

    # Check if folder can be deleted
    folder_size = calculate_folder_size(node)
    if folder_size >= required_limit:
        result = folder_size

    # Check if subfolders can be deleted
    for content in node.values():
        if not isinstance(content, dict):
            continue

        content_result = find_top_directory(content, required_limit)
        if content_result is not None and (result is None or content_result < result):
            result = content_result

    return result


def find_and_sum_by_top_size_limit(data, top_limit=100000):
    root = create_tree(data)
    accumulated_size = find_top_sizes(root, top_limit)
    return accumulated_size


def find_directory_to_remove(data, filesystem=70000000, required=30000000):
    root = create_tree(data)

    actual_used_space = calculate_folder_size(root)

    unused_space = filesystem - actual_used_space
    required_limit = required - unused_space

    result = find_top_directory(root, required_limit)
    return result


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return find_and_sum_by_top_size_limit(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return find_directory_to_remove(data)
