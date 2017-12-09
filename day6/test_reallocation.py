import unittest
from reallocation import Reallocation


class ReallocationTest(unittest.TestCase):

    def setUp(self):
        self.reallocation = Reallocation('0 2 7 0')

    def test_part_one(self):
        self.assertEqual(5, self.reallocation.solve_part_one())

    def test_part_two(self):
        self.assertEqual(4, self.reallocation.solve_part_two())

if __name__ == '__main__':
    unittest.main()
