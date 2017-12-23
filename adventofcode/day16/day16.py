import re
import string
from day import Day


class Programs:

    SPIN_REGEX = r's(\d+)'
    EXCHANGE_REGEX = r'x(\d+)/(\d+)'
    PARTNER_REGEX = r'p(\w)/(\w)'

    def __init__(self, size, moves):
        self.size = size
        self.moves = moves

    def dance(self, programs=None):
        # Initial standing of the programs
        if programs is None:
            programs = string.ascii_lowercase[:self.size]
        # Work with list as str is immutable
        programs = list(programs)
        for move in self.moves:
            spin = re.match(Programs.SPIN_REGEX, move)
            exchange = re.match(Programs.EXCHANGE_REGEX, move)
            partner = re.match(Programs.PARTNER_REGEX, move)
            if spin:
                n = int(spin.group(1))
                programs = Programs.spin(n, programs)
            if exchange:
                i = int(exchange.group(1))
                j = int(exchange.group(2))
                programs = Programs.exchange(i, j, programs)
            if partner:
                a = partner.group(1)
                b = partner.group(2)
                programs = Programs.partner(a, b, programs)
        return ''.join(programs)

    # Find a cycle and then compute the standing of the programs
    def n_dance(self, n):
        dances = []
        programs = self.dance()
        # Dance until we encounter a repeated standing
        while programs not in dances:
            dances.append(programs)
            programs = self.dance(programs)
        # The first element of dances is the standing after 1st dance
        return dances[(n-1) % len(dances)]

    @staticmethod
    def spin(n, programs):
        return programs[-n:] + programs[:-n]

    @staticmethod
    def exchange(i, j, programs):
        programs[i], programs[j] = programs[j], programs[i]
        return programs

    @staticmethod
    def partner(a, b, programs):
        i = programs.index(a)
        j = programs.index(b)
        return Programs.exchange(i, j, programs)


class Day16(Day):

    def __init__(self, moves, size=16):
        self.moves = moves.split(',')
        self.size = size

    def solve_part_one(self):
        return Programs(self.size, self.moves).dance()

    def solve_part_two(self):
        return Programs(self.size, self.moves).n_dance(10**9)
