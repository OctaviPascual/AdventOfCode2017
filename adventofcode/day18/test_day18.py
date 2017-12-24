import unittest
from day18.day18 import Day18


class Day17Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        program = [
            'set a 1',
            'add a 2',
            'mul a a',
            'mod a 5',
            'snd a',
            'set a 0',
            'rcv a',
            'jgz a -1',
            'set a 1',
            'jgz a -2'
        ]
        cls.day18 = Day18('\n'.join(program))

    def test_part_one(self):
        self.assertEqual(4, self.day18.solve_part_one())

    def test_part_two(self):
        pass
        #self.assertEqual(1222153, self.day18.solve_part_two())


if __name__ == '__main__':
    unittest.main()
