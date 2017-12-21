from itertools import cycle
from collections import defaultdict
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
        return [
            self.up(), self.down(), self.right(), self.left(),
            Square(self.x-1, self.y-1), Square(self.x-1, self.y+1),
            Square(self.x+1, self.y-1), Square(self.x+1, self.y+1)
        ]

    def distance(self, square):
        return abs(self.x - square.x) + abs(self.y - square.y)


class Memory:

    def __init__(self, target):
        self.target = int(target)
        self.directions = [Square.right, Square.up, Square.left, Square.down]
        self.initial_square = Square(0, 0)
        self.part_one = self.solve_part_one()
        self.part_two = self.solve_part_two()

    def solve_part_one(self):

        current_square = self.initial_square
        squares_to_move = 1
        data = 1
        moves = cycle(self.directions)

        # Emulate the spiral movement
        while True:
            for _ in range(2):
                move = next(moves)
                for _ in range(squares_to_move):
                    if data == self.target:
                        return current_square.distance(self.initial_square)
                    current_square = move(current_square)
                    data += 1
            squares_to_move += 1

    def solve_part_two(self):

        current_square = self.initial_square
        squares_to_move = 1
        moves = cycle(self.directions)
        memory = defaultdict(int)
        memory[current_square] = 1

        while True:
            for _ in range(2):
                move = next(moves)
                for _ in range(squares_to_move):
                    if memory[current_square] > self.target:
                        return memory[current_square]
                    current_square = move(current_square)
                    adjacent_squares = current_square.adjacent()
                    # This is where defaultdict comes in handy
                    data = sum(map(lambda x: memory[x], adjacent_squares))
                    memory[current_square] = data
            squares_to_move += 1


class Day03(Day):

    def __init__(self, target):
        self.memory = Memory(target)

    def solve_part_one(self):
        return self.memory.part_one

    def solve_part_two(self):
        return self.memory.part_two
