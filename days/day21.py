import common

DATA_FILE = 'day21.txt'
EXAMPLE_FILE = 'day21-example.txt'


def foo(data):
    lst = []
    for line in data:
        name, expression = line.split(': ')
        lst.append((name, expression))

    variables = {}
    pending = True
    while pending:
        pending = False
        for name, expression in lst:
            try:
                variables[name] = eval(expression, None, variables)
            except NameError as e:
                if e.args[0].startswith('name') and e.args[0].endswith('is not defined'):
                    pending = True
                    continue
                else:
                    raise e

    print(variables)
    return variables['root']


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return foo(data)


def part_2(input_file):
    raise NotImplementedError
