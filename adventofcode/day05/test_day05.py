import unittest
from day05.day05 import Day05


class Day05Test(unittest.TestCase):

    def test_part_one(self):
        instructions = ['0', '3', '0', '1', '-3']
        self.assertEqual(5, Day05('\n'.join(instructions)).solve_part_one())

    def test_part_two(self):
        instructions = ['0', '3', '0', '1', '-3']
        self.assertEqual(10, Day05('\n'.join(instructions)).solve_part_two())


if __name__ == '__main__':
    unittest.main()
