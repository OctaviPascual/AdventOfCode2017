import unittest
from day18.day18 import Day18


class Day18Test(unittest.TestCase):

    def test_part_one(self):
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
        self.assertEqual(4, Day18('\n'.join(program)).solve_part_one())

    def test_part_two(self):
        program = [
            'snd 1',
            'snd 2',
            'snd p',
            'rcv a',
            'rcv b',
            'rcv c',
            'rcv d'
        ]
        self.assertEqual(3, Day18('\n'.join(program)).solve_part_two())


if __name__ == '__main__':
    unittest.main()
