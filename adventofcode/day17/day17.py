from collections import deque
from day import Day


class Spinlock:

    def __init__(self, steps, times):
        self.steps = steps
        self.times = times
        self.buffer = deque([0])

    # Use deque rotation to emulate moving index
    def iterate(self, value):
        # Move to the right (thus rotate to the left) step times
        self.buffer.rotate(-self.steps)
        # Since the value is inserted to the right, rotate an extra step
        self.buffer.rotate(-1)
        # Insert the value to the left so it becomes the current position
        self.buffer.appendleft(value)

    def solve_part_one(self):
        for i in range(1, self.times+1):
            self.iterate(i)
        # The last value inserted is the front of the buffer,
        # so the value after it is the second element
        return self.buffer[1]

    # 0 value is in the buffer from the beginning, so we can
    # just track when the value after the 0 changes and we
    # do not even need to implement the buffer
    def solve_part_two(self):
        current_position = 0
        after_0 = None
        for i in range(1, self.times+1):
            current_position = (current_position + self.steps) % i + 1
            if current_position == 1:
                after_0 = i
        return after_0


class Day17(Day):

    def __init__(self, steps):
        self.steps = int(steps)

    def solve_part_one(self):
        return Spinlock(self.steps, 2017).solve_part_one()

    def solve_part_two(self):
        return Spinlock(self.steps, 50 * 10**6).solve_part_two()
