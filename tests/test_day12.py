import days.day12 as day


class TestDay12:
    def _test_find_fewest_steps(self):
        data = (x for x in [
            'Sxmmmmmmmaaaaaabbbccccddddeeemmmmaaa',
            'axmmmmmmlllkkkjjjiiihhhgggfffmmmmccc',
            'bxmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm',
            'cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'dxxxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuxxx',
            'exxxuuuuuuuuuuuuuuuuuuuuuuuuuuuuuxxx',
            'fxxxuuuxxxxxxxxxxxxxxxxxxxxxxxxxtxxx',
            'fxxxuuuxxxxxxxxxxxxxxxxxxxxxxxxxsxxx',
            'fxxxuuuuuuuuuuuuuuuvwxyzExxxxxxxrxxx',
            'fxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxqxxx',
            'fffffffffffffffffffffffghijklmnopxxx',
            'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        ])
        result = day.find_fewest_steps(data)
        assert result == 94

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 31

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result != 352
        assert result != 362
        assert result < 352
        assert result == 350

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 29

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 349
