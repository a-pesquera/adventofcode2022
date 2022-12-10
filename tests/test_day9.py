import days.day9 as day


class TestDay9:
    def test_calculate_tail_movement(self):
        examples = [
            ((0, 0), (0, 0), (0, 0)),
            ((1, 0), (0, 0), (0, 0)),
            ((2, 0), (0, 0), (1, 0)),
            ((1, 1), (0, 0), (0, 0)),
            ((2, 1), (0, 0), (1, 1)),
            ((2, 2), (0, 0), (1, 1)),
            ((6, 4), (4, 4), (5, 4)),
            ((6, 5), (4, 4), (5, 5)),
        ]
        for head, tail, expected in examples:
            result = day.calculate_tail_movement(head, tail)
            assert result == expected

    def test_count_tail_visited_positions(self):
        data = (x for x in [
            'R 4',
        ])
        result = day.count_tail_visited_positions(data)
        assert result == 4

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 13

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 6197

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 1

    def test_part_2_example(self):
        data = (x for x in [
            'R 5',
            'U 8',
            'L 8',
            'D 3',
            'R 17',
            'D 10',
            'L 25',
            'U 20',
        ])
        result = day.count_tail_visited_positions(data, rope_length=10)
        assert result == 36

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 2562
