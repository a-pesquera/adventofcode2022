import days.day3 as day


class TestDay3:
    def test_find_error(self):
        result = day.find_error('abcAbC')
        assert result == 'b'

    def test_find_common(self):
        result = day.find_common(['abcAbC', 'qwertC', 'poilCk'])
        assert result == 'C'

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 157

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 7875

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 70

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 2479
