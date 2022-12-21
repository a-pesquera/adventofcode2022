import days.day20 as day


class TestDay20:
    def test_move_turn(self):
        lst = [
            ([4, 5, 6, 1, 7, 8, 9], 3, [4, 5, 6, 7, 1, 8, 9]),
            ([4, -2, 5, 6, 7, 8, 9], 1, [4, 5, 6, 7, 8, -2, 9]),

            ([1, 2, 3, -8], 0, [2, 1, 3, -8]),
            ([1, 2, 3, -8], 1, [1, 3, -8, 2]),
            ([1, 2, 3, -8], 2, [1, 2, 3, -8]),
            ([1, 2, 3, -8], 3, [1, -8, 2, 3]),

            ([4, -2, 5, 6, 7, 8, 9], 0, [-2, 5, 6, 7, 4, 8, 9]),
            ([4, -2, 5, 6, 7, 8, 9], 2, [4, 5, -2, 6, 7, 8, 9]),
            ([4, -2, 5, 6, 7, 8, 9], 3, [4, -2, 5, 6, 7, 8, 9]),

            ([1, 2, -2, -3, 0, 3, 4], 2, [1, 2, -3, 0, 3, 4, -2]),
        ]
        for initial, index, expected in lst:
            result = day.move_turn(initial, index)
            assert result == expected

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 3

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 17490

    def _test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 0

    def _test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 0
