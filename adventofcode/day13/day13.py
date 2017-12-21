import re
from collections import defaultdict
from day import Day


class Firewall:

    REGEX = r'(\d+): (\d+)'

    def __init__(self, layers):
        self.firewall = self.build_firewall(layers)

    def build_firewall(self, layers):
        firewall = defaultdict(int)
        for layer in layers:
            search = re.search(Firewall.REGEX, layer)
            depth = int(search.group(1))
            scope = int(search.group(2))
            firewall[depth] = scope
        return firewall

    def trip(self, offset=0):
        picosecond = offset
        severity = 0
        trip_length = max(self.firewall) + 1
        for depth in range(trip_length):
            scope = self.firewall[depth]
            if scope > 0 and picosecond % (2*scope - 2) == 0:
                # Fail fast for part 2
                if depth == 0 and offset > 0:
                    return 9999
                # Fail fast for part 2
                if offset > 0 and severity > 0:
                    return 9999
                severity += depth*scope
            picosecond += 1
        return severity

    def trip2(self, offset=0):
        severity = 0
        for depth, scope in self.firewall.items():
            if (depth + offset) % (2*scope - 2) == 0:
                if depth == 0 and offset > 0:
                    return 99
                if offset > 0 and severity > 0:
                    return 99
                severity += depth*scope
        return severity

    # TODO: Implement efficient solution
    def solve2(self):
        p = 0
        while True:
            severity = self.trip2(p)
            if severity == 0:
                return p
            p += 1


class Day13(Day):

    def __init__(self, layers):
        layers = [p for p in layers.split('\n')]
        self.firewall = Firewall(layers)

    def solve_part_one(self):
        return self.firewall.trip2()

    def solve_part_two(self):
        return self.firewall.solve2()
