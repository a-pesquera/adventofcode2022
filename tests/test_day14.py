import days.day14 as day


class TestDay14:
    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 24

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 774

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 93

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 22499
