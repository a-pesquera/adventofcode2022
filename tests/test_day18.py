import days.day18 as day


class TestDay18:
    SMALL_EXAMPLE = ['1,1,1', '2,1,1']
    SMALL_EXAMPLE_EXTENDED = ['1,1,1', '2,1,1', '3,1,1']
    SMALL_SHAPE_V = ['1,1,1', '2,1,1', '1,2,1']
    ONE_HOLLOW = ['0,0,1', '0,0,-1', '0,1,0', '0,-1,0', '1,0,0', '-1,0,0']
    NO_HOLLOW = ['0,0,0', '0,0,1', '0,0,-1', '0,1,0', '0,-1,0', '1,0,0', '-1,0,0']
    CUBE_SIZE_2 = [
        '0,0,0',
        '0,0,1',
        '0,1,0',
        '0,1,1',

        '1,0,0',
        '1,0,1',
        '1,1,0',
        '1,1,1',
    ]
    CUBE_SIZE_3 = [
        '0,0,0',
        '0,0,1',
        '0,0,2',
        '0,1,0',
        '0,1,1',
        '0,1,2',
        '0,2,0',
        '0,2,1',
        '0,2,2',

        '1,0,0',
        '1,0,1',
        '1,0,2',
        '1,1,0',
        '1,1,1',
        '1,1,2',
        '1,2,0',
        '1,2,1',
        '1,2,2',

        '2,0,0',
        '2,0,1',
        '2,0,2',
        '2,1,0',
        '2,1,1',
        '2,1,2',
        '2,2,0',
        '2,2,1',
        '2,2,2',
    ]
    CUBE_SIZE_3_HOLLOW = [
        '0,0,0',
        '0,0,1',
        '0,0,2',
        '0,1,0',
        '0,1,1',
        '0,1,2',
        '0,2,0',
        '0,2,1',
        '0,2,2',

        '1,0,0',
        '1,0,1',
        '1,0,2',
        '1,1,0',
        # '1,1,1',
        '1,1,2',
        '1,2,0',
        '1,2,1',
        '1,2,2',

        '2,0,0',
        '2,0,1',
        '2,0,2',
        '2,1,0',
        '2,1,1',
        '2,1,2',
        '2,2,0',
        '2,2,1',
        '2,2,2',
    ]
    SHAPE_U = [
        '0,0,0',
        '0,0,1',
        '0,0,2',
        '0,1,0',
        # '0,1,1',
        # '0,1,2',
        '0,2,0',
        '0,2,1',
        '0,2,2',

        '1,0,0',
        '1,0,1',
        '1,0,2',
        '1,1,0',
        # '1,1,1',
        # '1,1,2',
        '1,2,0',
        '1,2,1',
        '1,2,2',

        '2,0,0',
        '2,0,1',
        '2,0,2',
        '2,1,0',
        # '2,1,1',
        # '2,1,2',
        '2,2,0',
        '2,2,1',
        '2,2,2',
    ]

    def test_count_surfaced_area_small_example(self):
        result = day.count_surfaced_area((x for x in self.SMALL_EXAMPLE))
        assert result == 10

    def test_count_surfaced_area_small_example_extended(self):
        result = day.count_surfaced_area((x for x in self.SMALL_EXAMPLE_EXTENDED))
        assert result == 14

    def test_count_surfaced_area_small_shape_v(self):
        result = day.count_surfaced_area((x for x in self.SMALL_SHAPE_V))
        assert result == 14

    def test_count_surfaced_area_one_hollow(self):
        result = day.count_surfaced_area((x for x in self.ONE_HOLLOW))
        assert result == 36

    def test_count_surfaced_area_no_hollow(self):
        result = day.count_surfaced_area((x for x in self.NO_HOLLOW))
        assert result == 30

    def test_count_surfaced_area_cube_size_2(self):
        result = day.count_surfaced_area((x for x in self.CUBE_SIZE_2))
        assert result == 24

    def test_count_surfaced_area_cube_size_3(self):
        result = day.count_surfaced_area((x for x in self.CUBE_SIZE_3))
        assert result == 54

    def test_count_surfaced_area_cube_size_3_hollow(self):
        result = day.count_surfaced_area((x for x in self.CUBE_SIZE_3_HOLLOW))
        assert result == 60

    def test_count_surfaced_area_shape_u(self):
        result = day.count_surfaced_area((x for x in self.SHAPE_U))
        assert result == 62

    def test_part_1_example(self):
        result = day.part_1(day.EXAMPLE_FILE)
        assert result == 64

    def test_part_1(self):
        result = day.part_1(day.DATA_FILE)
        assert result == 3326

    def test_count_exterior_surfaced_area_small_example(self):
        result = day.count_exterior_surfaced_area((x for x in self.SMALL_EXAMPLE))
        assert result == 10

    def test_count_exterior_surfaced_area_small_example_extended(self):
        result = day.count_exterior_surfaced_area((x for x in self.SMALL_EXAMPLE_EXTENDED))
        assert result == 14

    def test_count_exterior_surfaced_area_small_shape_v(self):
        result = day.count_exterior_surfaced_area((x for x in self.SMALL_SHAPE_V))
        assert result == 14

    def test_count_exterior_surfaced_area_one_hollow(self):
        result = day.count_exterior_surfaced_area((x for x in self.ONE_HOLLOW))
        assert result == 30

    def test_count_exterior_surfaced_area_no_hollow(self):
        result = day.count_exterior_surfaced_area((x for x in self.NO_HOLLOW))
        assert result == 30

    def test_count_exterior_surfaced_area_cube_size_2(self):
        result = day.count_exterior_surfaced_area((x for x in self.CUBE_SIZE_2))
        assert result == 24

    def test_count_exterior_surfaced_area_cube_size_3(self):
        result = day.count_exterior_surfaced_area((x for x in self.CUBE_SIZE_3))
        assert result == 54

    def test_count_exterior_surfaced_area_cube_size_3_hollow(self):
        result = day.count_exterior_surfaced_area((x for x in self.CUBE_SIZE_3_HOLLOW))
        assert result == 54

    def test_count_exterior_surfaced_area_shape_u(self):
        result = day.count_exterior_surfaced_area((x for x in self.SHAPE_U))
        assert result == 62

    def test_part_2_example(self):
        result = day.part_2(day.EXAMPLE_FILE)
        assert result == 58

    def test_part_2(self):
        result = day.part_2(day.DATA_FILE)
        assert result == 1996
