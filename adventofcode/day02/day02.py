from itertools import combinations
from day import Day


class Checksum:

    def __init__(self, spreadsheet):
        self.spreadsheet = spreadsheet
        self.part_one = self.solve_part_one()
        self.part_two = self.solve_part_two()

    def solve_part_one(self):
        result = 0
        for row in self.spreadsheet:
            result += max(row) - min(row)
        return result

    def solve_part_two(self):
        result = 0
        for row in self.spreadsheet:
            for a, b in combinations(row, 2):
                if a % b == 0:
                    result += a // b
                if b % a == 0:
                    result += b // a
        return result


class Day02(Day):

    def __init__(self, spreadsheet):
        spreadsheet = [row.split('\t') for row in spreadsheet.splitlines()]
        spreadsheet = [list(map(int, row)) for row in spreadsheet]
        self.checksum = Checksum(spreadsheet)

    def solve_part_one(self):
        return self.checksum.part_one

    def solve_part_two(self):
        return self.checksum.part_two
