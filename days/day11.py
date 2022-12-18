# @TODO future: retry without using class

from functools import reduce

import common

DATA_FILE = 'day11.txt'
EXAMPLE_FILE = 'day11-example.txt'


class Monkey:
    def __init__(self, items, operation_fn, divisible_by, indexes, too_much_worried):
        self.items = items
        self.operation_fn = operation_fn
        self.divisible_by = divisible_by
        self.too_much_worried = too_much_worried
        self.monkey_index_on_true = indexes[0]
        self.monkey_index_on_false = indexes[1]

        self.least_common_multiple = None

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

            if not self.too_much_worried:
                item = item // 3

            # Keep number "low"
            item = item % self.least_common_multiple

            test_result = item % self.divisible_by == 0
            if test_result:
                self.throw_to(self.monkey_on_true, item)
            else:
                self.throw_to(self.monkey_on_false, item)


def create_monkey(items_raw, operation_raw, test_raw, iftrue_raw, iffalse_raw, too_much_worried):
    # Process items
    items = [int(x) for x in items_raw[16:].split(', ')]

    # Process operation_fn
    operation = operation_raw[21:]

    contains_number = not operation.endswith('old')
    n = int(operation[2:]) if contains_number else None

    operation_fn = lambda old, n=n: old + n
    if operation.startswith('*'):
        if contains_number:
            operation_fn = lambda old, n=n: old * n
        else:
            operation_fn = lambda old: old * old

    # Process divisible_by
    divisible_by = int(test_raw[19:])

    # Process indexes of other monkeys
    monkey_on_true_idx = int(iftrue_raw[25:])
    monkey_on_false_idx = int(iffalse_raw[26:])

    # Create monkey and store references to other monkeys
    monkey = Monkey(items, operation_fn, divisible_by, (monkey_on_true_idx, monkey_on_false_idx), too_much_worried)
    return monkey


def create_monkeys_list(data, too_much_worried):
    monkeys = []
    throw_to_indexes = []
    numbers = []

    has_data = True
    while has_data:
        # Irrelevant initial line
        _ = next(data)
        items_raw = next(data)
        operation_raw = next(data)
        test_raw = next(data)
        iftrue_raw = next(data)
        iffalse_raw = next(data)

        try:
            # Irrelevant separation line
            _ = next(data)
        except StopIteration:
            has_data = False

        monkey = create_monkey(items_raw, operation_raw, test_raw, iftrue_raw, iffalse_raw, too_much_worried)
        monkeys.append(monkey)
        throw_to_indexes.append((monkey.monkey_index_on_true, monkey.monkey_index_on_false))
        numbers.append(monkey.divisible_by)

    # Calculate the LCM (least common multiple) to reduce worry levels
    # All input divisible_by are prime numbers
    least_common_multiple = reduce(lambda x, y: x * y, numbers, 1)

    # Assign monkeys to throw and LCM
    for i, monkey in enumerate(monkeys):
        true_idx = monkey.monkey_index_on_true
        false_idx = monkey.monkey_index_on_false
        monkeys[i].set_monkeys(monkeys[true_idx], monkeys[false_idx])

        monkeys[i].least_common_multiple = least_common_multiple

    return monkeys


def play_keep_away(data, rounds=20, num_top=2, too_much_worried=False):
    monkeys = create_monkeys_list(data, too_much_worried=too_much_worried)

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.play_turn()

    sorted_monkeys = sorted(monkeys, reverse=True, key=lambda m: m.num_inspected_items)
    top_monkeys = sorted_monkeys[:num_top]
    top_num_inspected_items = (x.num_inspected_items for x in top_monkeys)
    product_result = reduce(lambda x, y: x * y, top_num_inspected_items, 1)
    return product_result


def part_1(input_file):
    data = common.read_data_file_generator(input_file)
    return play_keep_away(data)


def part_2(input_file):
    data = common.read_data_file_generator(input_file)
    return play_keep_away(data, rounds=10000, too_much_worried=True)
