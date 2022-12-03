import days.day1 as day


class TestDay1:
    def test_small(self):
        data = (x for x in ['2', '5', '10', '', '4'])
        result = day.elf_with_max_weight(data)
        assert result == 17

    def test_part_1_example(self):
        result = day.part_1('day1-example.txt')
        assert result == 24000

    def test_part_1(self):
        result = day.part_1('day1.txt')
        assert result == 67016

    def test_part_2_example(self):
        result = day.part_2('day1-example.txt')
        assert result == 45000

    def test_part_2(self):
        result = day.part_2('day1.txt')
        assert result == 200116
