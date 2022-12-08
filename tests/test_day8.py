import days.day8 as day


class TestDay8:
    def test_count_visible_trees_left(self):
        data = (x for x in [
            '999',
            '159',
            '999',
        ])
        result = day.count_visible_trees(data)
        assert result == 9

    def test_count_visible_trees_right(self):
        data = (x for x in [
            '999',
            '951',
            '999',
        ])
        result = day.count_visible_trees(data)
        assert result == 9

    def test_count_visible_trees_top(self):
        data = (x for x in [
            '919',
            '959',
            '999',
        ])
        result = day.count_visible_trees(data)
        assert result == 9

    def test_count_visible_trees_bottom(self):
        data = (x for x in [
            '999',
            '959',
            '919',
        ])
        result = day.count_visible_trees(data)
        assert result == 9

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 21

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 1708

    def _test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 42

    def _test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 42
