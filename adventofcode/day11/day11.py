from day import Day


class Hexagon:

    # Cube coordinates: https://www.redblobgames.com/grids/hexagons/#coordinates-cube
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def north(self):
        return Hexagon(self.x, self.y+1, self.z-1)

    def northeast(self):
        return Hexagon(self.x+1, self.y, self.z-1)

    def southeast(self):
        return Hexagon(self.x+1, self.y-1, self.z)

    def south(self):
        return Hexagon(self.x, self.y-1, self.z+1)

    def southwest(self):
        return Hexagon(self.x-1, self.y, self.z+1)

    def northwest(self):
        return Hexagon(self.x-1, self.y+1, self.z)

    def distance(self, hexagon):
        return max(abs(self.x - hexagon.x),
                   abs(self.y - hexagon.y),
                   abs(self.z - hexagon.z))


class HexagonGrid:

    INITIAL_HEXAGON = Hexagon(x=0, y=0, z=0)

    DIRECTIONS = {
        'n' : Hexagon.north,
        'ne': Hexagon.northeast,
        'se': Hexagon.southeast,
        's' : Hexagon.south,
        'sw': Hexagon.southwest,
        'nw': Hexagon.northwest
    }

    def __init__(self, path):
        self.path = path
        self.final_dist = None
        self.furthest_dist = 0
        self.run()

    def run(self):
        current_hex = HexagonGrid.INITIAL_HEXAGON

        for direction in self.path:
            current_hex = HexagonGrid.DIRECTIONS[direction](current_hex)
            current_dist = current_hex.distance(HexagonGrid.INITIAL_HEXAGON)
            self.furthest_dist = max(current_dist, self.furthest_dist)

        self.final_dist = current_hex.distance(HexagonGrid.INITIAL_HEXAGON)


class Day11(Day):

    def __init__(self, path):
        path = [p for p in path.split(',')]
        self.hexagon_grid = HexagonGrid(path)

    def solve_part_one(self):
        return self.hexagon_grid.final_dist

    def solve_part_two(self):
        return self.hexagon_grid.furthest_dist
