import re

import common

DATA_FILE = 'day7.txt'
EXAMPLE_FILE = 'day7-example.txt'

STEP_RE = re.compile(r'^(\d+) (.+)$')


def create_folder(name, parent):
    path = (parent['path'] if parent else '') + name + '/'
    folder = {
        'name': name,
        'path': path,
        'folders': [],
        'files': [],
        'size': 0,
        'parent': parent,
    }
    if parent:
        parent['folders'].append(folder)
    return folder


def increase_folder_size(folder, size):
    folder['size'] += size
    if folder['parent']:
        increase_folder_size(folder['parent'], size)


def add_file(folder, name, size):
    folder['files'].append({
        'name': name,
        'path': folder['path'] + '/' + name,
        'size': size,
    })
    increase_folder_size(folder, size)




def print_tree(node, level=0):
    prefix = level * 2 * ' ' + '-'
    file_prefix = (level + 1) * 2 * ' ' + '-'

    name = node['name'] or '/'
    print(prefix, f'{name} (dir, size={node["size"]})')
    for folder in node['folders']:
        print_tree(folder, level + 1)
    for file in node['files']:
        print(file_prefix, f'{file["name"]} (file, size={file["size"]})')



def create_tree(data):
    # at most 100000
    # sum of their total sizes is 95437
    first_line = next(data)
    if first_line != '$ cd /':
        raise Exception('Unexpected initial line')

    root = create_folder('', None)
    actual = root

    for line in data:
        if line == '$ cd ..':
            # Go 1 down
            actual = actual['parent'] or actual
        elif line.startswith('$ cd '):
            # Go 1 up
            folder_name = line[5:]
            folder = create_folder(folder_name, actual)
            actual = folder
        elif line == '$ ls' or line.startswith('dir '):
            # Irrelevant
            pass
        else:
            # Is "ls" output for files
            size, name =  STEP_RE.match(line).groups()
            add_file(actual, name, int(size))

    return root


def find_and_sum_by_top_size_limit(data, top_limit=100000):
    root = create_tree(data)
    # print_tree(root)

    result = 0

    pending_folders = root['folders']
    while pending_folders:
        folder = pending_folders.pop()
        pending_folders.extend(folder['folders'])
        if folder['size'] <= top_limit:
            result += folder['size']

    return result


def find_directory_to_remove(data, filesystem=70000000, required=30000000):
    root = create_tree(data)
    # print_tree(root)

    unused_space = filesystem - root['size']
    required_limit = required - unused_space

    candidates = []

    pending_folders = [root]
    while pending_folders:
        folder = pending_folders.pop()
        if folder['size'] >= required_limit:
            candidates.append(folder)
            pending_folders.extend(folder['folders'])

    folder = min(candidates, key=lambda x: x['size'])
    return folder['size']


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return find_and_sum_by_top_size_limit(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return find_directory_to_remove(data)
