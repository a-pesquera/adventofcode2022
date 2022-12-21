import common

DATA_FILE = 'day21.txt'
EXAMPLE_FILE = 'day21-example.txt'


def run_calculations(lst, variables):
    has_new_variable = True
    while has_new_variable:
        has_new_variable = False

        delete_from_lst_indexes = []
        for i, (name, expression) in enumerate(lst):
            if name in variables:
                continue
            try:
                variables[name] = eval(expression, None, variables)
                has_new_variable = True
                delete_from_lst_indexes.append(i)
            except NameError as e:
                if e.args[0].startswith('name') and e.args[0].endswith('is not defined'):
                    continue
                raise e

        # Delete already done expressions
        for i in reversed(delete_from_lst_indexes):
            lst.pop(i)


def run_calculations_reversing_expressions(lst, variables):
    # Invert explanation (second in tuple):
    # "foo = bar * baz" transforms to "baz = foo / bar". Most of the cases new left is old equal.
    # But "foo = bar / baz" transforms to "baz = bar / foo", so new *right* is equal, that's why
    # the is_inverted is true only for "-" and "/".
    operations_transform_left = {
        '+': ('-', False),
        '-': ('-', True),
        '*': ('/', False),
        '/': ('/', True),
    }
    operations_transform_right = {
        '+': ('-', False),
        '-': ('+', False),
        '*': ('/', False),
        '/': ('*', False),
    }

    while lst:
        # Create new expressions
        delete_from_lst_indexes = []
        append_to_lst = []
        for i, (name, expression) in enumerate(lst):
            if name not in variables:
                continue

            left, operation, right = expression.split(' ')
            if left in variables:
                new_operation, is_inverted = operations_transform_left[operation]
                new_name = right
                new_left = name
                new_right = left
            else:
                new_operation, is_inverted = operations_transform_right[operation]
                new_name = left
                new_left = name
                new_right = right

            new_expression = f'{new_left} {new_operation} {new_right}'
            if is_inverted:
                new_expression = f'{new_right} {new_operation} {new_left}'

            delete_from_lst_indexes.append(i)
            append_to_lst.append((new_name, new_expression))

        # Delete transformed expressions
        for i in reversed(delete_from_lst_indexes):
            lst.pop(i)

        # Generate new variables using new reversed expressions
        lst.extend(append_to_lst)
        run_calculations(lst, variables)


def calculate_root_value(data):
    lst = []
    for line in data:
        name, expression = line.split(': ')
        lst.append((name, expression))

    variables = {}
    run_calculations(lst, variables)

    return variables['root']


def calculate_humn_value(data):
    lst = []

    # Obtain root equal variables and ignore humn
    root_parts = None
    for line in data:
        name, expression = line.split(': ')
        if name == 'root':
            left, *_, right = expression.split(' ')
            root_parts = (left, right)
            continue
        elif name == 'humn':
            continue
        lst.append((name, expression))

    # Like part 1 creating variables but not all will be set
    variables = {}
    run_calculations(lst, variables)

    # Set root left-right value in variables
    if root_parts[0] in variables:
        variables[root_parts[1]] = variables[root_parts[0]]
    else:
        variables[root_parts[0]] = variables[root_parts[1]]

    # Now go for the final result transforming the expressions
    run_calculations_reversing_expressions(lst, variables)

    return variables['humn']


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return calculate_root_value(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return calculate_humn_value(data)
