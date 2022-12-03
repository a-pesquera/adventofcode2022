import os.path


def get_data_filepath(file):
    return os.path.join(os.path.dirname(__file__), 'data', file)


def read_data_file_generator(file):
    file_path = get_data_filepath(file)
    with open(file_path) as f:
        for l in f:
            yield l.strip()
