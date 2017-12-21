import unittest
from day06.day06 import Day06


class Day06Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.day06 = Day06('0 2 7 0')

    def test_part_one(self):
        self.assertEqual(5, self.day06.solve_part_one())

    def test_part_two(self):
        self.assertEqual(4, self.day06.solve_part_two())


if __name__ == '__main__':
    unittest.main()
