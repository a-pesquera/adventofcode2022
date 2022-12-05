import days.day5 as day


class TestDay5:
    def test_parse_two_stacks(self):
        lines = [
            '    [A]',
            '[B] [C]',
        ]
        result = day.parse_stacks(lines)
        assert result == [['B'], ['C', 'A']]

    def test_parse_three_stacks_with_one_empty(self):
        lines = [
            '[B]     [X]',
        ]
        result = day.parse_stacks(lines)
        assert result == [['B'], [], ['X']]

    def test_parse_step_single(self):
        result = day.parse_step('move 1 from 2 to 1')
        assert result == [(2, 1)]

    def test_parse_step_multi(self):
        result = day.parse_step('move 3 from 13 to 42')
        assert result == [(13, 42), (13, 42), (13, 42)]

    def test_do_step(self):
        stacks = [['B'], [], ['X']]
        step = (1, 2)
        result = day.do_step(stacks, step)
        assert result == [[], ['B'], ['X']]

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 'CMZ'

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 'JDTMRWCQJ'

    def _test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 0

    def _test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 0
