import unittest
from day07.day07 import Day07


class Day07Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        tower = [
            'pbga (66)',
            'xhth (57)',
            'ebii (61)',
            'havc (66)',
            'ktlj (57)',
            'fwft (72) -> ktlj, cntj, xhth',
            'qoyq (66)',
            'padx (45) -> pbga, havc, qoyq',
            'tknk (41) -> ugml, padx, fwft',
            'jptl (61)',
            'ugml (68) -> gyxo, ebii, jptl',
            'gyxo (61)',
            'cntj (57)'
        ]
        cls.day07 = Day07('\n'.join(tower))

    def test_part_one(self):
        self.assertEqual('tknk', self.day07.solve_part_one())

    def test_part_two(self):
        self.assertEqual(60, self.day07.solve_part_two())


if __name__ == '__main__':
    unittest.main()
