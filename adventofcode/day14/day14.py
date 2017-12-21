from day10.day10 import KnotHash
from day import Day


class Square:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash( (self.x, self.y) )

    def up(self):
        return Square(self.x, self.y+1)

    def down(self):
        return Square(self.x, self.y-1)

    def right(self):
        return Square(self.x+1, self.y)

    def left(self):
        return Square(self.x-1, self.y)

    def adjacent(self):
        return [self.up(), self.down(), self.right(), self.left()]


class Disk:

    def __init__(self, key, size):
        self.key = key
        self.size = size
        bits = self.build_bits()
        self.grid = self.build_grid(bits)

    def build_bits(self):
        rows = [self.key + '-' + str(i) for i in range(self.size)]
        knot_hashes = list(map(lambda x: KnotHash(x), rows))
        hashes = []
        for h in knot_hashes:
            h.execute()
            hashes.append(h.hash)
        width = str(self.size)
        return [('{0:0' + width + 'b}').format(int(h, 16)) for h in hashes]

    def build_grid(self, bits):
        grid = {}
        for x in range(self.size):
            for y in range(self.size):
                grid[Square(x, y)] = '#' if bits[x][y] == '1' else '.'
        return grid

    def used_squares(self):
        return list(self.grid.values()).count('#')

    def dfs(self, square, visited):
        if square not in visited and square in self.grid and self.grid[square] == '#':
            visited.add(square)
            for neighbor in square.adjacent():
                self.dfs(neighbor, visited)

    def regions(self):
        total_regions = 0
        visited = set()
        to_visit = {square for square in self.grid if self.grid[square] == '#'}
        while to_visit:
            # Retrieve a square that has not been visited yet
            square = next(iter(to_visit))
            self.dfs(square, visited)
            # Remove visited squares from to_visit set
            to_visit.difference_update(visited)
            total_regions += 1
        return total_regions


class Day14(Day):

    def __init__(self, key, size=128):
        self.disk = Disk(key, size)

    def solve_part_one(self):
        return self.disk.used_squares()

    def solve_part_two(self):
        return self.disk.regions()
