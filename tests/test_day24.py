import days.day24 as day


class TestDay24:
    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 18

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 295

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 54

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result > 740
        assert result == 851
