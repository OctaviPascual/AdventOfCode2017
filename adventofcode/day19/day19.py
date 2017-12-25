import sys
from day import Day


class Cell:

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __hash__(self):
        return hash( (self.i, self.j) )

    def up(self):
        return Cell(self.i-1, self.j)

    def down(self):
        return Cell(self.i+1, self.j)

    def right(self):
        return Cell(self.i, self.j+1)

    def left(self):
        return Cell(self.i, self.j-1)


class Diagram:

    def __init__(self, diagram):
        self.initial_cell = Cell(0, diagram[0].index('|'))
        self.diagram = {}
        self.build_diagram(diagram)
        self.letters = ''
        self.steps = 0
        self.advance(self.initial_cell, Cell.down)

    def build_diagram(self, diagram):
        for i in range(len(diagram)):
            for j in range(len(diagram[i])):
                self.diagram[Cell(i, j)] = diagram[i][j]

    def is_allowed(self, cell):
        return cell in self.diagram and self.diagram[cell] != ' '

    def advance(self, cell, direction):

        self.steps += 1

        if self.diagram[cell].isalpha():
            self.letters += self.diagram[cell]

        # First we try to advance in the same direction
        next_cell = direction(cell)
        if self.is_allowed(next_cell):
            self.advance(next_cell, direction)
            return

        # If not possible, then we have to change the direction

        # If the we were moving in a vertical direction,
        # we must change to a horizontal one
        if direction in [Cell.up, Cell.down]:
            left_cell = cell.left()
            right_cell = cell.right()
            if self.is_allowed(left_cell):
                self.advance(left_cell, Cell.left)
            elif self.is_allowed(right_cell):
                self.advance(right_cell, Cell.right)

        # Conversely, if the we were moving horizontally,
        # we must change to a vertical direction
        if direction in [Cell.left, Cell.right]:
            up_cell = cell.up()
            down_cell = cell.down()
            if self.is_allowed(up_cell):
                self.advance(up_cell, Cell.up)
            elif self.is_allowed(down_cell):
                self.advance(down_cell, Cell.down)


class Day19(Day):

    def __init__(self, diagram):
        # We use a recursive function to solve this problem
        sys.setrecursionlimit(100000)
        self.diagram = diagram.splitlines()

    def solve_part_one(self):
        return Diagram(self.diagram).letters

    def solve_part_two(self):
        return Diagram(self.diagram).steps
