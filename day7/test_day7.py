import unittest
from day7 import Day7


class Day7Test(unittest.TestCase):

    def setUp(self):
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
        self.day7 = Day7('\n'.join(tower))

    def test_part_one(self):
        self.assertEqual(self.day7.solve_part_one(), 'tknk')

    def test_part_two(self):
        self.assertEqual(self.day7.solve_part_two(), 60)

if __name__ == '__main__':
    unittest.main()
