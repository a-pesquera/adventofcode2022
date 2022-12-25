import days.day25 as day


class TestDay25:
    def test_decimal_to_snafu(self):
        examples = [
            (1, '1'),
            (2, '2'),
            (3, '1='),
            (4, '1-'),
            (5, '10'),
            (6, '11'),
            (7, '12'),
            (8, '2='),
            (9, '2-'),
            (10, '20'),
            (15, '1=0'),
            (20, '1-0'),
            (2022, '1=11-2'),
            (12345, '1-0---0'),
            (314159265, '1121-1110-1=0'),
        ]
        for decimal, snafu in examples:
            calculated = day.decimal_to_snafu(decimal)
            assert calculated == snafu

    def test_snafu_to_decimal(self):
        examples = [
            ('1', 1),
            ('2', 2),
            ('1=', 3),
            ('1-', 4),
            ('10', 5),
            ('11', 6),
            ('12', 7),
            ('2=', 8),
            ('2-', 9),
            ('20', 10),
            ('1=0', 15),
            ('1-0', 20),
            ('1=11-2', 2022),
            ('1-0---0', 12345),
            ('1121-1110-1=0', 314159265),
        ]
        for snafu, decimal in examples:
            calculated = day.snafu_to_decimal(snafu)
            assert calculated == decimal

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == '2=-1=0'

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == '2=0=02-0----2-=02-10'

    def _test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 0

    def _test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 0
