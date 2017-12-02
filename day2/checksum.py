from itertools import combinations

class Checksum:

    def __init__(self, spreadsheet):
        spreadsheet = [row.split('\t') for row in spreadsheet.split('\n')]
        self.spreadsheet = [list(map(int, row)) for row in spreadsheet]        

    def solve_part_one(self):
        result = 0
        for row in self.spreadsheet:
            result += max(row) - min(row)
        return result

    def solve_part_two(self):
        result = 0
        for row in self.spreadsheet:
            for a,b in combinations(row, 2):
                if a%b == 0: result += a // b
                if b%a == 0: result += b // a
        return result
