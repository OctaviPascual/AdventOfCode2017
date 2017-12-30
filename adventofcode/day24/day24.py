from copy import deepcopy
from day import Day


class Component:

    def __init__(self, component):
        self.a, self.b = map(int, component.split('/'))

    def sum(self):
        return self.a + self.b

    def matches(self, bridge):
        return self.a == bridge.last_port[-1] or self.b == bridge.last_port[-1]


class Bridge:

    def __init__(self):
        self.strength = 0
        self.last_port = [0]
        self.components = []

    def __len__(self):
        return len(self.components)

    def strongest(self, other):
        return other if self.strength < other.strength else self

    def longest(self, other):
        if len(self) == len(other):
            return self.strongest(other)
        return other if len(self) < len(other) else self

    def add_component(self, component):
        self.components.append(component)
        self.strength += component.sum()
        if self.last_port[-1] == component.a:
            self.last_port.append(component.b)
        else:
            self.last_port.append(component.a)

    def remove_component(self):
        if not self.components:
            raise IndexError('The bridge has no components')
        self.last_port.pop()
        component = self.components.pop()
        self.strength -= component.sum()


class BridgeBuilder:

    def __init__(self, components):
        # This is needed to track the best bridges found so far
        self.bridges = {
            'strongest': Bridge(),
            'longest': Bridge()
        }
        self.build_bridge(components, Bridge.strongest, 'strongest')
        self.build_bridge(components, Bridge.longest, 'longest')

    # This function is a basic backtracking to find the best bridge
    def build_bridge(self, components, comparison, key, bridge=Bridge()):

        # deepcopy() is an expensive operation, so we must be careful and
        # minimize the number of calls
        # We only update the result if we find a better bridge
        if self.bridges[key] != comparison(self.bridges[key], bridge):
            self.bridges[key] = deepcopy(bridge)

        candidates = [c for c in components if c.matches(bridge)]
        for candidate in candidates:
            bridge.add_component(candidate)
            components.remove(candidate)
            self.build_bridge(components, comparison, key, bridge)
            components.append(candidate)
            bridge.remove_component()


class Day24(Day):

    def __init__(self, components):
        self.builder = BridgeBuilder([Component(c) for c in components.splitlines()])

    def solve_part_one(self):
        return self.builder.bridges['strongest'].strength

    def solve_part_two(self):
        return self.builder.bridges['longest'].strength
