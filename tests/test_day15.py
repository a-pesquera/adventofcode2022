import pytest

import days.day15 as day


class TestDay15:
    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE, check_y=10)
        assert result == 26

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE, check_y=2000000)
        assert result == 5127797

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE, limit=20)
        assert result == 56000011

    @pytest.mark.skip('Slow test')
    def test_part_2(self):
        result = day.part_2(day.DATA_FILE, limit=4_000_000)
        assert result == 12518502636475
