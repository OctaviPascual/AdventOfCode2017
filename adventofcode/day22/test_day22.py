import unittest
from day22.day22 import Day22


class Day22Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.grid = [
            '..#',
            '#..',
            '...',
        ]

    def test_part_one(self):
        self.assertEqual(5, Day22('\n'.join(self.grid), 7).solve_part_one())
        self.assertEqual(41, Day22('\n'.join(self.grid), 70).solve_part_one())
        self.assertEqual(5587, Day22('\n'.join(self.grid)).solve_part_one())

    def test_part_two(self):
        self.assertEqual(26, Day22('\n'.join(self.grid), 100).solve_part_two())
        self.assertEqual(2511944, Day22('\n'.join(self.grid)).solve_part_two())


if __name__ == '__main__':
    unittest.main()
