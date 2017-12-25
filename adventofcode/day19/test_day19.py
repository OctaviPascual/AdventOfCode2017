import unittest
from day19.day19 import Day19


class Day20Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        diagram = [
            '     |',
            '     |  +--+',
            '     A  |  C',
            ' F---|----E|--+',
            '     |  |  |  D',
            '     +B-+  +--+',
            ''
        ]
        cls.day19 = Day19('\n'.join(diagram))

    def test_part_one(self):
        self.assertEqual('ABCDEF', self.day19.solve_part_one())

    def test_part_two(self):
        self.assertEqual(38, self.day19.solve_part_two())


if __name__ == '__main__':
    unittest.main()
