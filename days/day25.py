import common

DATA_FILE = 'day25.txt'
EXAMPLE_FILE = 'day25-example.txt'


SNAFU_MAPPING = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2,
}


def decimal_to_snafu(number):
    # print('number', number)

    size = None
    tmp = 0
    for i in range(number):
        tmp += 5 ** i * 2
        # print('Max with', i, 'pow:', tmp)
        if number <= tmp:
            size = i + 1
            break

    # print('size', size)

    result = ''

    while len(result) != size:
        new_c = '2'
        for c in '10-=':
            # print('c', c)
            tmp_snafu = result + c + '2' * (size - 1 - len(result))
            # print('tmp_snafu', tmp_snafu)
            tmp_decimal = snafu_to_decimal(tmp_snafu)
            # print('tmp_decimal', tmp_decimal)
            if tmp_decimal >= number:
                new_c = c
            else:
                break

        result += new_c
        # print('result', result)

    return result


def snafu_to_decimal(snafu):
    result = 0
    for i, c in enumerate(reversed(snafu)):
        result += 5 ** i * SNAFU_MAPPING[c]
    return result


def foo(data):
    decimal_result = 0
    for line in data:
        decimal_result += snafu_to_decimal(line)
    result = decimal_to_snafu(decimal_result)
    return result


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return foo(data)


def part_2(input_file):
    raise NotImplementedError
