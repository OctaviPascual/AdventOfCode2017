import unittest
from day25.day25 import Day25


class Day25Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        blueprint = [
            'Begin in state A.',
            'Perform a diagnostic checksum after 6 steps.',
            '',
            'In state A:',
            '  If the current value is 0:',
            '    - Write the value 1.',
            '    - Move one slot to the right.',
            '    - Continue with state B.',
            '  If the current value is 1:',
            '    - Write the value 0.'
            '    - Move one slot to the left.',
            '    - Continue with state B.',
            '',
            'In state B:',
            '  If the current value is 0:',
            '    - Write the value 1.',
            '    - Move one slot to the left.',
            '    - Continue with state A.',
            '  If the current value is 1:',
            '    - Write the value 1.'
            '    - Move one slot to the right.',
            '    - Continue with state A.',
        ]
        cls.day25 = Day25('\n'.join(blueprint))

    def test_part_one(self):
        self.assertEqual(3, self.day25.solve_part_one())

    def test_part_two(self):
        pass

if __name__ == '__main__':
    unittest.main()
