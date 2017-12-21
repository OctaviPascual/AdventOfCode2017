import unittest
from day08.day08 import Day08


class Day8Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        instructions = [
            'b inc 5 if a > 1',
            'a inc 1 if b < 5',
            'c dec -10 if a >= 1',
            'c inc -20 if c == 10'
        ]
        cls.day08 = Day08('\n'.join(instructions))

    def test_part_one(self):
        self.assertEqual(1, self.day08.solve_part_one())

    def test_part_two(self):
        self.assertEqual(10, self.day08.solve_part_two())


if __name__ == '__main__':
    unittest.main()
