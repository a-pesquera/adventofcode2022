import days.day7 as day


class TestDay7:
    def test_find_and_sum_by_top_size_limit_0(self):
        data = (x for x in [
            '$ cd /',
            '$ cd foo',
            '$ cd bar',
            '$ cd foo',
            '$ cd bar',
            '$ cd foo',
            '$ cd bar',
            '$ cd ..',
            '$ cd ..',
            '$ cd ..',
            '$ cd ..',
            '$ cd ..',
            '$ cd ..',
            '$ cd ..',
            '$ cd ..',
            '$ cd ..',
        ])
        result = day.find_and_sum_by_top_size_limit(data)
        assert result == 0

    def test_find_and_sum_by_top_size_limit_1(self):
        data = (x for x in [
            '$ cd /',
            '$ ls',
            'dir foo',
            'dir bar',
            '$ cd foo',
            '$ ls',
            '123 a',
            '456 b',
            '789 c.txt',
            '$ cd ..',
            '$ cd bar',
            '$ ls',
            '123000 a',
            '456000 b',
            '789000 c.txt',
        ])
        result = day.find_and_sum_by_top_size_limit(data)
        assert result == 1368

    def test_find_and_sum_by_top_size_limit_2_recount(self):
        data = (x for x in [
            '$ cd /',
            '$ ls',
            'dir foo',
            '$ cd foo',
            '$ ls',
            'dir bar',
            '123 a',
            '456 b',
            '789 c.txt',
            '$ cd bar',
            '$ ls',
            '123 a',
            '456 b',
            '789 c.txt',
        ])
        result = day.find_and_sum_by_top_size_limit(data)
        assert result == 4104

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 95437

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 1845346

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 24933642

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 3636703
