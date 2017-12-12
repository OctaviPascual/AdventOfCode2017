import unittest
from day12 import Day12


class Day11Test(unittest.TestCase):

    def setUp(self):
        programs = [
            '0 <-> 2',
            '1 <-> 1',
            '2 <-> 0, 3, 4',
            '3 <-> 2, 4',
            '4 <-> 2, 3, 6',
            '5 <-> 6',
            '6 <-> 4, 5'
        ]
        self.programs = '\n'.join(programs)

    def test_part_one(self):
        self.assertEqual(6, Day12(self.programs).solve_part_one())

    def test_part_two(self):
        self.assertEqual(2, Day12(self.programs).solve_part_two())


if __name__ == '__main__':
    unittest.main()
