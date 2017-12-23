import unittest
from day16.day16 import Day16


class Day16Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        moves = ['s1', 'x3/4', 'pe/b']
        cls.day16 = Day16(','.join(moves), 5)

    def test_part_one(self):
        self.assertEqual('baedc', self.day16.solve_part_one())

    def test_part_two(self):
        self.assertEqual('abcde', self.day16.solve_part_two())


if __name__ == '__main__':
    unittest.main()
