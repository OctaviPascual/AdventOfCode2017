import unittest
from day02.day02 import Day02


class Day02Test(unittest.TestCase):

    def test_part_one(self):
        spreadsheet = [
            '5\t1\t9\t5',
            '7\t5\t3',
            '2\t4\t6\t8'
        ]
        self.assertEqual(18, Day02('\n'.join(spreadsheet)).solve_part_one())

    def test_part_two(self):
        spreadsheet = [
            '5\t9\t2\t8',
            '9\t4\t7\t3',
            '3\t8\t6\t5'
        ]
        self.assertEqual(9, Day02('\n'.join(spreadsheet)).solve_part_two())


if __name__ == '__main__':
    unittest.main()
