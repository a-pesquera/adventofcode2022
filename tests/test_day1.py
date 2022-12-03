import days.day1


class TestDay1:
    def test_small(self):
        data = (x for x in ['2', '5', '10', '', '4'])
        result = days.day1.function(data)
        assert result == 17

    def test_example(self):
        result = days.day1.part1('day1-example.txt')
        assert result == 24000

    def test_part_1(self):
        result = days.day1.part1('day1.txt')
        assert result == 67016
