import unittest
from day17.day17 import Day17


class Day17Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.day17 = Day17('3')

    def test_part_one(self):
        self.assertEqual(638, self.day17.solve_part_one())

    def test_part_two(self):
        self.assertEqual(1222153, self.day17.solve_part_two())


if __name__ == '__main__':
    unittest.main()
