import days.day23 as day


class TestDay23:
    def test_example_small(self):
        data = (x for x in [
            '.....',
            '..##.',
            '..#..',
            '.....',
            '..##.',
            '.....',
        ])
        result, *_ = day.plant_seeds(data, rounds=5)
        assert result == 25

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE, rounds=10)
        assert result == 110

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE, rounds=10)
        assert result == 4068

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 20

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result > 624
        assert result == 968
