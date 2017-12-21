import unittest
from day03.day03 import Day03


class Day03Test(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(0, Day03('1').solve_part_one())
        self.assertEqual(3, Day03('12').solve_part_one())
        self.assertEqual(2, Day03('23').solve_part_one())
        self.assertEqual(31, Day03('1024').solve_part_one())

    def test_part_two(self):
        self.assertEqual(2, Day03('1').solve_part_two())
        self.assertEqual(133, Day03('130').solve_part_two())
        self.assertEqual(806, Day03('800').solve_part_two())


if __name__ == '__main__':
    unittest.main()
