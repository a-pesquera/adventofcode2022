from functools import reduce

import common

DATA_FILE = 'day11.txt'
EXAMPLE_FILE = 'day11-example.txt'


class Monkey:
    def __init__(self, items, operation_fn, test_fn):
        self.items = items
        self.operation_fn = operation_fn
        self.test_fn = test_fn
        self.monkey_on_true = None
        self.monkey_on_false = None
        self.num_inspected_items = 0

    def __repr__(self):
        return f'{{Monkey: {self.items} [{self.num_inspected_items}]}}'

    def set_monkeys(self, monkey_on_true, monkey_on_false):
        self.monkey_on_true = monkey_on_true
        self.monkey_on_false = monkey_on_false

    def throw_to(self, monkey, item):
        monkey.items.append(item)

    def play_turn(self):
        while self.items:
            self.num_inspected_items += 1

            item = self.items.pop(0)
            item = self.operation_fn(item)
            item = item // 3
            test_result = self.test_fn(item)
            if test_result:
                self.throw_to(self.monkey_on_true, item)
            else:
                self.throw_to(self.monkey_on_false, item)


def create_monkeys_list(data):
    monkeys = []
    throw_to_indexes = []

    has_data = True
    while has_data:
        # Irrelevant line
        _ = next(data)
        items_raw = next(data)
        operation_raw = next(data)
        test_raw = next(data)
        iftrue_raw = next(data)
        iffalse_raw = next(data)

        try:
            # Irrelevant new line
            _ = next(data)
        except StopIteration:
            has_data = False

        # Process items
        items = [int(x) for x in items_raw[16:].split(', ')]

        # Process operation_fn
        operation = operation_raw[21:]
        is_old = operation.endswith('old')
        n = None
        if not is_old:
            n = int(operation[2:])
        operation_fn = None
        if operation.startswith('+'):
            if is_old:
                operation_fn = lambda old: old + old
            else:
                operation_fn = lambda old, n=n: old + n
        elif operation.startswith('*'):
            if is_old:
                operation_fn = lambda old: old * old
            else:
                operation_fn = lambda old, n=n: old * n
        else:
            raise NotImplementedError

        # Process test_fn
        divisible_by = int(test_raw[19:])
        test_fn = lambda item, n=divisible_by: item % n == 0

        # Create monkey and store references to other monkeys
        monkey = Monkey(items, operation_fn, test_fn)
        monkeys.append(monkey)

        monkey_on_true_idx = int(iftrue_raw[25:])
        monkey_on_false_idx = int(iffalse_raw[26:])
        throw_to_indexes.append((monkey_on_true_idx, monkey_on_false_idx))

    # Assign monkeys to throw
    for i, (true_idx, false_idx) in enumerate(throw_to_indexes):
        monkeys[i].set_monkeys(monkeys[true_idx], monkeys[false_idx])

    return monkeys


def play_keep_away(data, rounds=20, num_top=2):
    monkeys = create_monkeys_list(data)

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.play_turn()

    sorted_monkeys = sorted(monkeys, reverse=True, key=lambda m: m.num_inspected_items)
    top_monkeys = sorted_monkeys[:num_top]
    top_num_inspected_items = (x.num_inspected_items for x in top_monkeys)
    multiply_result = reduce(lambda x, y: x * y, top_num_inspected_items, 1)
    return multiply_result


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return play_keep_away(data)


def part_2(input_file):
    raise NotImplementedError
