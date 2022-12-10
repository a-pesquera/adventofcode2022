import days.day10 as day


class TestDay10:
    def test_part_1_example_small(self):
        data = (x for x in [
            'noop',
            'addx 3',
            'addx -5',
        ])
        result = day.sum_of_signals(data)
        assert result == 0

    def test_part_1_example_part(self):
        data = (x for x in [
            'addx 15',
            'addx -11',
            'addx 6',
            'addx -3',
            'addx 5',
            'addx -1',
            'addx -8',
            'addx 13',
            'addx 4',
            'noop',
            'addx -1',
            'addx 5',
            'addx -1',
        ])
        result = day.sum_of_signals(data)
        assert result == 420

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 13140

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 14420

    def _test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 0

    def _test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 0
