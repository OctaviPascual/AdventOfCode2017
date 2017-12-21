import unittest
from day11.day11 import Day11


class Day11Test(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(3, Day11('ne,ne,ne').solve_part_one())
        self.assertEqual(0, Day11('ne,ne,sw,sw').solve_part_one())
        self.assertEqual(2, Day11('ne,ne,s,s').solve_part_one())
        self.assertEqual(3, Day11('se,sw,se,sw,sw').solve_part_one())

    def test_part_two(self):
        self.assertEqual(3, Day11('ne,ne,ne').solve_part_two())
        self.assertEqual(2, Day11('ne,ne,sw,sw').solve_part_two())
        self.assertEqual(2, Day11('ne,ne,s,s').solve_part_two())
        self.assertEqual(3, Day11('se,sw,se,sw,sw').solve_part_two())


if __name__ == '__main__':
    unittest.main()
