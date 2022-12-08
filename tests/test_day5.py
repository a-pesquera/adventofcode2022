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

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 'CMZ'

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 'JDTMRWCQJ'

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 'MCD'

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 'VHJDDCWRD'
