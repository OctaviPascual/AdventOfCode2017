import re
from day import Day


class Village:

    REGEX = r'(\d+) <-> (.*)'

    def __init__(self, programs):
        self.village = self.build_graph(programs)

    def build_graph(self, programs):
        village = {}
        for program in programs:
            search = re.search(Village.REGEX, program)
            id = int(search.group(1))
            neighbors = [int(x.strip()) for x in search.group(2).split(',')]
            village[id] = neighbors
        return village

    def dfs(self, program, visited):
        if program not in visited:
            visited.add(program)
            for neighbor in self.village[program]:
                self.dfs(neighbor, visited)

    def group(self, start):
        visited = set()
        self.dfs(start, visited)
        return visited

    def groups(self):
        visited = set()
        total_groups = 0
        while len(visited) < len(self.village):
            # Retrieve a program that has not been visited yet
            start = next(iter(set(self.village.keys()) - visited))
            visited.update(self.group(start))
            total_groups += 1
        return total_groups


class Day12(Day):

    def __init__(self, programs):
        programs = [p for p in programs.splitlines()]
        self.village = Village(programs)

    def solve_part_one(self):
        return len(self.village.group(0))

    def solve_part_two(self):
        return self.village.groups()
