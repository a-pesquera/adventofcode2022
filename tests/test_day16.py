import pytest

import days.day16 as day


class TestDay16:
    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 1651

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 1724

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 1707

    @pytest.mark.skip('Slow test')
    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result > 2121
        assert result == 2283
