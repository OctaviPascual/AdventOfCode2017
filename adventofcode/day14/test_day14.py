import unittest
from day14.day14 import Day14


class Day14Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.day14 = Day14('flqrgnkx')

    def test_part_one(self):
        self.assertEqual(8108, self.day14.solve_part_one())

    def test_part_two(self):
        self.assertEqual(1242, self.day14.solve_part_two())


if __name__ == '__main__':
    unittest.main()
