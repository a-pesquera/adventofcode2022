import days.day13 as day


class TestDay13:
    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 13

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 5185

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 140

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 23751
