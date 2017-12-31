import re
from day import Day


class Firewall:

    REGEX = re.compile(r'(\d+): (\d+)')

    def __init__(self, layers):
        self.firewall = self.build_firewall(layers)

    def build_firewall(self, layers):
        firewall = {}
        for layer in layers:
            match = Firewall.REGEX.match(layer)
            depth = int(match.group(1))
            scope = int(match.group(2))
            firewall[depth] = scope
        return firewall

    def trip(self):
        severity = 0
        for depth, scope in self.firewall.items():
            if depth % (2*scope - 2) == 0:
                severity += depth*scope
        return severity

    def is_caught(self, delay):
        for depth, scope in self.firewall.items():
            if (depth + delay) % (2*scope - 2) == 0:
                return True
        return False

    def trip_with_delay(self):
        delay = 0
        while True:
            if not self.is_caught(delay):
                return delay
            delay += 1


class Day13(Day):

    def __init__(self, layers):
        layers = [p for p in layers.splitlines()]
        self.firewall = Firewall(layers)

    def solve_part_one(self):
        return self.firewall.trip()

    def solve_part_two(self):
        return self.firewall.trip_with_delay()
