from day import Day


class Maze:

    def __init__(self, instructions):
        self.instructions = instructions

    def solve_part_one(self):
        maze = self.instructions.copy()
        position = steps = 0
        while self.inside_maze(position):
            offset = maze[position]
            maze[position] += 1
            position = self.jump(position, offset)
            steps += 1
        return steps

    # This is horrendously slow, but it seems intrinsic to Python
    def solve_part_two(self):
        maze = self.instructions.copy()
        position = steps = 0
        # Surprisingly storing the length saves me about 2 seconds
        n = len(maze)
        # And avoiding helper functions also saves time
        while 0 <= position < n:
            offset = maze[position]
            maze[position] += 1 if offset < 3 else -1
            position += offset
            steps += 1
        return steps

    def inside_maze(self, i):
        return 0 <= i < len(self.instructions)

    def jump(self, position, offset):
        return position + offset


class Day05(Day):

    def __init__(self, instructions):
        instructions = [int(x) for x in instructions.splitlines()]
        self.maze = Maze(instructions)

    def solve_part_one(self):
        return self.maze.solve_part_one()

    def solve_part_two(self):
        return self.maze.solve_part_two()
