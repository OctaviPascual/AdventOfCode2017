import unittest
from day8 import Day8


class Day8Test(unittest.TestCase):

    def setUp(self):
        instructions = [
            'b inc 5 if a > 1',
            'a inc 1 if b < 5',
            'c dec -10 if a >= 1',
            'c inc -20 if c == 10'
        ]
        self.day8 = Day8('\n'.join(instructions))

    def test_part_one(self):
        self.assertEqual(self.day8.solve_part_one(), 1)

    def test_part_two(self):
        self.assertEqual(self.day8.solve_part_two(), 10)

if __name__ == '__main__':
    unittest.main()
