import days.day4 as day


class TestDay4:
    def test_count_assignments_fully_contains_not_overlap(self):
        data = (x for x in ['1-2,3-4'])
        result = day.count_assignments_fully_contains(data)
        assert result == 0

    def test_count_assignments_fully_contains_partial_overlap(self):
        data = (x for x in ['1-3,3-4'])
        result = day.count_assignments_fully_contains(data)
        assert result == 0

    def test_count_assignments_fully_contains_full_overlap(self):
        data = (x for x in ['1-4,3-4'])
        result = day.count_assignments_fully_contains(data)
        assert result == 1

    def test_count_assignments_fully_contains_full_overlap_but_second(self):
        data = (x for x in ['1-1,1-4'])
        result = day.count_assignments_fully_contains(data)
        assert result == 1

    def test_count_assignments_overlaps_not_overlap(self):
        data = (x for x in ['1-2,3-4'])
        result = day.count_assignments_overlaps(data)
        assert result == 0

    def test_count_assignments_overlaps_partial_overlap(self):
        data = (x for x in ['1-3,3-4'])
        result = day.count_assignments_overlaps(data)
        assert result == 1

    def test_count_assignments_overlaps_full_overlap(self):
        data = (x for x in ['1-4,3-4'])
        result = day.count_assignments_overlaps(data)
        assert result == 1

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 2

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 483

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 4

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 874
