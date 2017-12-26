from enum import Enum
from collections import defaultdict
from day import Day


class Direction(Enum):

    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    @staticmethod
    def turn_right(direction):
        if direction == Direction.UP:    return Direction.RIGHT
        if direction == Direction.RIGHT: return Direction.DOWN
        if direction == Direction.DOWN:  return Direction.LEFT
        if direction == Direction.LEFT:  return Direction.UP
        raise ValueError("Invalid direction: {}".format(direction))

    @staticmethod
    def turn_left(direction):
        if direction == Direction.UP:    return Direction.LEFT
        if direction == Direction.LEFT:  return Direction.DOWN
        if direction == Direction.DOWN:  return Direction.RIGHT
        if direction == Direction.RIGHT: return Direction.UP
        raise ValueError("Invalid direction: {}".format(direction))

    @staticmethod
    def reverse(direction):
        if direction == Direction.UP:    return Direction.DOWN
        if direction == Direction.LEFT:  return Direction.RIGHT
        if direction == Direction.DOWN:  return Direction.UP
        if direction == Direction.RIGHT: return Direction.LEFT
        raise ValueError("Invalid direction: {}".format(direction))


class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash( (self.x, self.y) )

    def up(self):
        return Node(self.x - 1, self.y)

    def down(self):
        return Node(self.x + 1, self.y)

    def right(self):
        return Node(self.x, self.y + 1)

    def left(self):
        return Node(self.x, self.y - 1)

    def move(self, direction):
        if direction == Direction.UP:    return self.up()
        if direction == Direction.RIGHT: return self.right()
        if direction == Direction.DOWN:  return self.down()
        if direction == Direction.LEFT:  return self.left()


class Cluster:

    def __init__(self, grid, bursts):
        self.bursts = bursts
        self.virus = None
        self.starting_node = None
        self.infections = 0
        self.grid = defaultdict(lambda: '.')
        self.fill_grid(grid)

    def fill_grid(self, grid):
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                self.grid[Node(i, j)] = grid[i][j]
        self.starting_node = Node(n // 2, m // 2)

    def start_infection(self):
        if self.virus is None:
            raise ValueError('Cannot start infection without virus')
        for _ in range(self.bursts):
            self.virus.burst()

    def is_node_infected(self, node):
        return self.grid[node] == '#'

    def is_node_clean(self, node):
        return self.grid[node] == '.'

    def is_node_flagged(self, node):
        return self.grid[node] == 'F'

    def is_node_weakened(self, node):
        return self.grid[node] == 'W'

    def infect_node(self, node):
        self.infections += 1
        self.grid[node] = '#'

    def clean_node(self, node):
        # Instead of setting the position as '.' I went for deleting
        # the key since the smaller we keep the grid the better.
        # Since the grid is a defaultdict with default value '.',
        # if the node is accessed later it will still have the correct value
        del self.grid[node]

    def flag_node(self, node):
        self.grid[node] = 'F'

    def weaken_node(self, node):
        self.grid[node] = 'W'

    def add_virus(self, virus):
        self.virus = virus


class Virus:

    def __init__(self, cluster):
        self.cluster = cluster
        self.current_node = cluster.starting_node
        self.direction = Direction.UP

    def update_direction(self):
        if self.cluster.is_node_infected(self.current_node):
            self.direction = self.direction.turn_right(self.direction)
        elif self.cluster.is_node_clean(self.current_node):
            self.direction = self.direction.turn_left(self.direction)
        else:
            raise ValueError('Current node state is unknown')

    def update_node_state(self):
        if self.cluster.is_node_infected(self.current_node):
            self.cluster.clean_node(self.current_node)
        elif self.cluster.is_node_clean(self.current_node):
            self.cluster.infect_node(self.current_node)
        else:
            raise ValueError('Current node state is unknown')

    def move(self, node, direction):
        self.current_node = node.move(direction)

    def burst(self):
        self.update_direction()
        self.update_node_state()
        self.move(self.current_node, self.direction)


# Inherit Virus class and only override two of its methods
# Finally inheritance comes handy :)
class EvolvedVirus(Virus):

    def update_direction(self):
        if self.cluster.is_node_infected(self.current_node):
            self.direction = self.direction.turn_right(self.direction)
        elif self.cluster.is_node_weakened(self.current_node):
            pass
        elif self.cluster.is_node_flagged(self.current_node):
            self.direction = self.direction.reverse(self.direction)
        elif self.cluster.is_node_clean(self.current_node):
            self.direction = self.direction.turn_left(self.direction)
        else:
            raise ValueError('Current node status is unknown')

    def update_node_state(self):
        if self.cluster.is_node_infected(self.current_node):
            self.cluster.flag_node(self.current_node)
        elif self.cluster.is_node_weakened(self.current_node):
            self.cluster.infect_node(self.current_node)
        elif self.cluster.is_node_flagged(self.current_node):
            self.cluster.clean_node(self.current_node)
        elif self.cluster.is_node_clean(self.current_node):
            self.cluster.weaken_node(self.current_node)
        else:
            raise ValueError('Current node status is unknown')


class Day22(Day):

    def __init__(self, grid, bursts=None):
        self.grid = grid.splitlines()
        self.bursts = bursts

    def solve_part_one(self):
        bursts = 10000 if self.bursts is None else self.bursts
        cluster = Cluster(self.grid, bursts)
        virus = Virus(cluster)
        cluster.add_virus(virus)
        cluster.start_infection()
        return cluster.infections

    def solve_part_two(self):
        bursts = 10000000 if self.bursts is None else self.bursts
        cluster = Cluster(self.grid, bursts)
        # Instead of a virus, create an EvolvedVirus, as easy as that
        virus = EvolvedVirus(cluster)
        cluster.add_virus(virus)
        cluster.start_infection()
        return cluster.infections
