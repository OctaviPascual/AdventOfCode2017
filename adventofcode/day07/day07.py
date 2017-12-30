import re
from day import Day


class Program:

    REGEX = re.compile(r'(\w+) \((\d+)\)(?: -> (.*))?')

    def __init__(self, row):
        match = self.REGEX.match(row)
        self.name = match.group(1)
        self.weight = int(match.group(2))
        self.children = []
        if match.group(3):
            self.children.extend([c.strip() for c in match.group(3).split(',')])


class Programs:

    def __init__(self, programs):
        self.programs = {program.name: program for program in programs}
        self.root = self.build_tree()
        self.suitable_weight = None
        self.find_suitable_weight(self.root)

    # This function constructs the tree and returns its root
    def build_tree(self):
        for program in self.programs.values():
            program.children = [self.programs[c] for c in program.children]

        # To find the root of the tree, we start at a random node and
        # we walk up until we find the only node without parent
        root_candidate = list(self.programs.values())[0]
        parent = self.find_parent(root_candidate)
        while parent is not None:
            root_candidate = parent
            parent = self.find_parent(root_candidate)
        return root_candidate

    def find_parent(self, root):
        for program in self.programs.values():
            if root in program.children:
                return program
        return None

    def find_suitable_weight(self, root):
        weights = {c: self.find_suitable_weight(c) for c in root.children}
        self.set_suitable_weight_if_needed(weights)
        return root.weight + sum(weights.values())

    # We perform a DFS on the tree, so we know that the first unbalanced
    # weight that we will find is the wrong weight
    def set_suitable_weight_if_needed(self, weights):

        if not weights or self.suitable_weight is not None:
            return

        min_weight = min(list(weights.values()))
        max_weight = max(list(weights.values()))
        if min_weight != max_weight:
            if list(weights.values()).count(min_weight) == 1:
                unbalanced, balanced = min_weight, max_weight
            else:
                unbalanced, balanced = max_weight, min_weight
            weight = [w.weight for w in weights if weights[w] == unbalanced][0]
            self.suitable_weight = weight + balanced - unbalanced


class Day07(Day):

    def __init__(self, tower):
        tower = [t for t in tower.splitlines()]
        self.programs = Programs([Program(row) for row in tower])

    def solve_part_one(self):
        return self.programs.root.name

    def solve_part_two(self):
        return self.programs.suitable_weight
