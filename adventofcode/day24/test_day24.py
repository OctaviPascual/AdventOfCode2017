import unittest
from day24.day24 import Day24


class Day24Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        components = [
            '0/2',
            '2/2',
            '2/3',
            '3/4',
            '3/5',
            '0/1',
            '10/1',
            '9/10'
        ]
        cls.day24 = Day24('\n'.join(components))

    def test_part_one(self):
        self.assertEqual(31, self.day24.solve_part_one())

    def test_part_two(self):
        self.assertEqual(19, self.day24.solve_part_two())

if __name__ == '__main__':
    unittest.main()
