import unittest
from reallocation import Reallocation


class ReallocationTest(unittest.TestCase):

    def setUp(self):
        self.reallocation = Reallocation('0 2 7 0')

    def test_part_one(self):
        self.assertEqual(self.reallocation.solve_part_one(), 5)

    def test_part_two(self):
        self.assertEqual(self.reallocation.solve_part_two(), 4)

if __name__ == '__main__':
    unittest.main()
