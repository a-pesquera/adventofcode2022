import days.day17 as day


class TestDay17:
    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 3068

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 3232

    def _test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 0

    def _test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 0
