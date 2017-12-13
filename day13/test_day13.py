import unittest
from day13 import Day13


class Day11Test(unittest.TestCase):

    def setUp(self):
        layers = [
            '0: 3',
            '1: 2',
            '4: 4',
            '6: 4'
        ]
        self.layers = '\n'.join(layers)

    def test_part_one(self):
        self.assertEqual(24, Day13(self.layers).solve_part_one())

    def test_part_two(self):
        self.assertEqual(10, Day13(self.layers).solve_part_two())


if __name__ == '__main__':
    unittest.main()
