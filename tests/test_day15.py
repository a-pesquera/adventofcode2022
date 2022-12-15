import days.day15 as day


class TestDay15:
    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE, check_y=10)
        assert result == 26

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE, check_y=2000000)
        assert result == 5127797

    def _test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 0

    def _test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 0
