import unittest
from day15.day15 import Day15


class Day15Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        starts = [
            'Generator A starts with 65',
            'Generator B starts with 8921'
        ]
        cls.day15 = Day15('\n'.join(starts))

    def test_part_one(self):
        pass
        #self.assertEqual(588, self.day15.solve_part_one())

    def test_part_two(self):
        self.assertEqual(309, self.day15.solve_part_two())


if __name__ == '__main__':
    unittest.main()
