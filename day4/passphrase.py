from itertools import combinations

class Passphrase:

    def __init__(self, passphrases):
        self.passphrases = [row.split() for row in passphrases.split('\n')]

    def solve_part_one(self):
        total = 0
        for row in self.passphrases:
            total += len(row) == len(set(row))
        return total

    def solve_part_two(self):
        total = 0
        for row in self.passphrases:
            total += 1
            for a,b in combinations(row, 2):
                if self.are_anagram(a, b):
                    total -= 1
                    break
        return total

    def are_anagram(self, a, b):
        return sorted(a) == sorted(b)
