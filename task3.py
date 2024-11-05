import unittest


def time_difference(time1, time2):
    diff = abs(time1 - time2)
    if diff > 12:
        diff = 24 - diff
    return diff


class TestTimeDifference(unittest.TestCase):

    def test_same_time(self):
        """
        Test that the difference between the same times is zero.
        """
        t1 = 5
        t2 = 5
        expected = 0
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)

    def test_opposite_times(self):
        """
        Test times that are exactly 12 hours apart.
        """
        t1 = 0
        t2 = 12
        expected = 12
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)

    def test_across_midnight(self):
        """
        Test times across midnight, e.g., 23:00 and 01:00.
        """
        t1 = 23
        t2 = 1
        expected = 2
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)

    def test_less_than_12_hours(self):
        """
        Test times where the difference is less than 12 hours.
        """
        t1 = 5
        t2 = 8
        expected = 3
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)

    def test_exactly_12_hours(self):
        """
        Test times where the difference is exactly 12 hours.
        """
        t1 = 6
        t2 = 18
        expected = 12
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)

    def test_just_over_12_hours(self):
        """
        Test times where the difference is just over 12 hours.
        """
        t1 = 6
        t2 = 19
        expected = 11  # Since abs(6 - 19) = 13, adjusted to 24 - 13 = 11
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)

    def test_edge_case_midnight(self):
        """
        Test the edge case where one time is at 0:00 and the other at 24:00.
        """
        t1 = 0
        t2 = 24  # 24 is equivalent to 0 in a 24-hour clock
        expected = 0
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)

    def test_fractional_hours(self):
        """
        Test times with fractional hours.
        """
        t1 = 10.5
        t2 = 13.75
        expected = 3.25  # abs(10.5 - 13.75) = 3.25
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)

    def test_times_wrapping_around(self):
        """
        Test times that wrap around the 24-hour mark.
        """
        t1 = 22
        t2 = 2
        expected = 4  # Since abs(22 - 2) = 20, adjusted to 24 - 20 = 4
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)

    def test_negative_times(self):
        """
        Test how the function handles negative time values.
        """
        t1 = -1
        t2 = 1
        expected = 2  # abs(-1 - 1) = 2
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)

    def test_times_exceeding_24_hours(self):
        """
        Test how the function handles times greater than 24 hours.
        """
        t1 = 25
        t2 = 1
        expected = 24  # abs(25 - 1) = 24, adjusted to 24 - 24 = 0
        result = time_difference(t1, t2)
        self.assertEqual(result, 0)

    def test_large_difference(self):
        """
        Test times with a large difference to ensure proper adjustment.
        """
        t1 = 5
        t2 = 20
        expected = 9  # abs(5 - 20) = 15, adjusted to 24 - 15 = 9
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)

    def test_minute_precision(self):
        """
        Test times with minute precision.
        """
        t1 = 10.75  # 10:45 AM
        t2 = 11.25  # 11:15 AM
        expected = 0.5  # 30 minutes difference
        result = time_difference(t1, t2)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
