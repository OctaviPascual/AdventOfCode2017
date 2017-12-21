import unittest
from day13.day13 import Day13


class Day13Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        layers = [
            '0: 3',
            '1: 2',
            '4: 4',
            '6: 4'
        ]
        cls.day13 = Day13('\n'.join(layers))

    def test_part_one(self):
        self.assertEqual(24, self.day13.solve_part_one())

    def test_part_two(self):
        self.assertEqual(10, self.day13.solve_part_two())


if __name__ == '__main__':
    unittest.main()
