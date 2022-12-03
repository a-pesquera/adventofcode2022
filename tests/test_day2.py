import days.day2 as day


class TestDay2:
    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 15

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 15632

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 12

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 14416
