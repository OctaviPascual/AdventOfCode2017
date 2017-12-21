import unittest
from day09.day09 import Day09


class Day9Test(unittest.TestCase):

    def test_part_one(self):
        streams = {
            '{}': 1,
            '{{{}}}': 6,
            '{{},{}}': 5,
            '{{{},{},{{}}}}': 16,
            '{<a>,<a>,<a>,<a>}': 1,
            '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
            '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
            '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3
        }
        for stream, expected in streams.items():
            self.assertEqual(expected, Day09(stream).solve_part_one())

    def test_part_two(self):
        streams = {
            '<>': 0,
            '<random characters>': 17,
            '<<<<>': 3,
            '<{!>}>': 2,
            '<!!>': 0,
            '<!!!>>': 0,
            '<{o"i!a,<{i<a>': 10
        }
        for stream, expected in streams.items():
            self.assertEqual(expected, Day09(stream).solve_part_two())


if __name__ == '__main__':
    unittest.main()
