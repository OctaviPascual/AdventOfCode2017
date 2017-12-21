import unittest
from day12.day12 import Day12


class Day12Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        programs = [
            '0 <-> 2',
            '1 <-> 1',
            '2 <-> 0, 3, 4',
            '3 <-> 2, 4',
            '4 <-> 2, 3, 6',
            '5 <-> 6',
            '6 <-> 4, 5'
        ]
        cls.day12 = Day12('\n'.join(programs))

    def test_part_one(self):
        self.assertEqual(6, self.day12.solve_part_one())

    def test_part_two(self):
        self.assertEqual(2, self.day12.solve_part_two())


if __name__ == '__main__':
    unittest.main()
