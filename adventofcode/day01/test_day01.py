import unittest
from day01.day01 import Day01


class Day01Test(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(3, Day01('1122').solve_part_one())
        self.assertEqual(4, Day01('1111').solve_part_one())
        self.assertEqual(0, Day01('1234').solve_part_one())
        self.assertEqual(9, Day01('91212129').solve_part_one())

    def test_part_two(self):
        self.assertEqual(6, Day01('1212').solve_part_two())
        self.assertEqual(0, Day01('1221').solve_part_two())
        self.assertEqual(4, Day01('123425').solve_part_two())
        self.assertEqual(4, Day01('12131415').solve_part_two())
        self.assertEqual(12, Day01('123123').solve_part_two())


if __name__ == '__main__':
    unittest.main()
