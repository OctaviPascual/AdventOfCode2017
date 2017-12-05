class Maze:

    def __init__(self, instructions):
        self.instructions = [int(x) for x in instructions.split('\n')]

    def solve_part_one(self):
        maze = self.instructions.copy()
        position = steps = 0
        while self.inside_maze(position):
            offset = maze[position]
            maze[position] += 1
            position = self.jump(position, offset)
            steps += 1
        return steps

    def solve_part_two(self):
        maze = self.instructions.copy()
        position = steps = 0
        while self.inside_maze(position):
            offset = maze[position]
            maze[position] += 1 if offset < 3 else -1
            position = self.jump(position, offset)
            steps += 1
        return steps

    def inside_maze(self, i):
        return 0 <= i < len(self.instructions)

    def jump(self, position, offset):
        return position + offset
