import unittest
from day04.day04 import Day04


class Day04Test(unittest.TestCase):

    def test_part_one(self):
        passphrases = [
            'aa bb cc dd ee',
            'aa bb cc dd aa',
            'aa bb cc dd aaa'
        ]
        self.assertEqual(2, Day04('\n'.join(passphrases)).solve_part_one())

    def test_part_two(self):
        passphrases = [
            'abcde fghij',
            'abcde xyz ecdab',
            'a ab abc abd abf abj',
            'iiii oiii ooii oooi oooo',
            'oiii ioii iioi iiio'
        ]
        self.assertEqual(3, Day04('\n'.join(passphrases)).solve_part_two())


if __name__ == '__main__':
    unittest.main()
