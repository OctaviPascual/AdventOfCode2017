import unittest
from day20.day20 import Day20


class Day20Test(unittest.TestCase):

    def test_part_one(self):
        particles = [
            'p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>',
            'p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>'
        ]
        self.assertEqual(0, Day20('\n'.join(particles)).solve_part_one())

    def test_part_two(self):
        particles = [
            'p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>',
            'p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>',
            'p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>',
            'p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>'
        ]
        self.assertEqual(1, Day20('\n'.join(particles)).solve_part_two())


if __name__ == '__main__':
    unittest.main()
