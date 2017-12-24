from itertools import combinations
from day import Day


class Passphrase:

    def __init__(self, passphrases):
        self.passphrases = passphrases

    def solve_part_one(self):
        total = 0
        for row in self.passphrases:
            total += len(row) == len(set(row))
        return total

    def solve_part_two(self):
        total = 0
        for row in self.passphrases:
            total += 1
            for a, b in combinations(row, 2):
                if self.are_anagram(a, b):
                    total -= 1
                    break
        return total

    def are_anagram(self, a, b):
        return sorted(a) == sorted(b)


class Day04(Day):

    def __init__(self, passphrases):
        passphrases = [row.split() for row in passphrases.splitlines()]
        self.passphrase = Passphrase(passphrases)

    def solve_part_one(self):
        return self.passphrase.solve_part_one()

    def solve_part_two(self):
        return self.passphrase.solve_part_two()
