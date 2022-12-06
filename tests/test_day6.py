import days.day6 as day


class TestDay6:
    def test_look_for_marker_multi(self):
        examples = [
            ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
            ('nppdvjthqldpwncqszvftbrmjlhg', 6),
            ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
            ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
        ]
        for line, expected in examples:
            result = day.look_for_marker(line)
            assert result == expected

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 7

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 1287

    def _test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 'MCD'

    def _test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 'VHJDDCWRD'
