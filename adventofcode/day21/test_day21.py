import unittest
from day21.day21 import Day21


class Day21Test(unittest.TestCase):

    def test_part_one(self):
        rules = [
            '../.# => ##./#../...',
            '.#./..#/### => #..#/..../..../#..#'
        ]
        self.assertEqual(12, Day21('\n'.join(rules), 2).solve_part_one())

    def test_part_two(self):
        # Unfortunately, for this problem there were no tests for part two :(
        pass


if __name__ == '__main__':
    unittest.main()
