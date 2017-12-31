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
        self.initial_direction = Cell.down
        self.diagram = {}
        self.build_diagram(diagram)
        self.letters = ''
        self.steps = 0
        self.solve()
        # I leave here the call to the original function
        #self.advance(self.initial_cell, self.initial_direction)

    def build_diagram(self, diagram):
        for i in range(len(diagram)):
            for j in range(len(diagram[i])):
                self.diagram[Cell(i, j)] = diagram[i][j]

    def is_allowed(self, cell):
        return cell in self.diagram and self.diagram[cell] != ' '

    def solve(self):
        current_cell = self.initial_cell
        direction = self.initial_direction
        while True:
            self.steps += 1

            if self.diagram[current_cell].isalpha():
                self.letters += self.diagram[current_cell]

            next_cell = direction(current_cell)
            if self.is_allowed(next_cell):
                current_cell = next_cell
                continue

            if direction in [Cell.up, Cell.down]:
                left_cell = current_cell.left()
                right_cell = current_cell.right()
                if self.is_allowed(left_cell):
                    current_cell, direction = left_cell, Cell.left
                    continue
                elif self.is_allowed(right_cell):
                    current_cell, direction = right_cell, Cell.right
                    continue

            if direction in [Cell.left, Cell.right]:
                up_cell = current_cell.up()
                down_cell = current_cell.down()
                if self.is_allowed(up_cell):
                    current_cell, direction = up_cell, Cell.up
                    continue
                elif self.is_allowed(down_cell):
                    current_cell, direction = down_cell, Cell.down
                    continue

            # If we reach this point, there are no more positions to move
            break

    # This is the initial recursive function that I used to solve this puzzle
    # It is a tail-recursive function and it looks like pypy does not like it,
    # since it gives a mysterious segmentation fault
    def advance(self, cell, direction):

        self.steps += 1

        if self.diagram[cell].isalpha():
            # Note that for long strings (which are immutable in Python)
            # it is much more efficient to use a list and perform
            # a ''.join(string) operation at the end, but in this case
            # since there are only 26 [A-Z] possible letters,
            # it is more convenient and readable to use += operation
            # http://blog.mclemon.io/python-efficient-string-concatenation-in-python-2016-edition
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
