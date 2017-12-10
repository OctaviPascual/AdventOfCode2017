import unittest
from day10 import Day10


class Day10Test(unittest.TestCase):

    def test_part_one(self):
        actual = Day10("3,4,1,5", 5).solve_part_one()
        self.assertEqual(12, actual)

    def test_part_two(self):
        actual = Day10('').solve_part_two()
        self.assertEqual('a2582a3a0e66e6e86e3812dcb672a272', actual)

        actual = Day10('AoC 2017').solve_part_two()
        self.assertEqual('33efeb34ea91902bb2f59c9920caa6cd', actual)

        actual = Day10('1,2,3').solve_part_two()
        self.assertEqual('3efbe78a8d82f29979031a4aa0b16a9d', actual)

        actual = Day10('1,2,4').solve_part_two()
        self.assertEqual('63960835bcdc130f0b66d7ff4f6a5a8e', actual)


if __name__ == '__main__':
    unittest.main()
