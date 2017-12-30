import re
import operator
from collections import defaultdict
from day import Day


class Instruction:

    REGEX = re.compile(
        r'(\w+) (\binc\b|\bdec\b) (-?\d+) \bif\b (\w+) ([<>=!]{1,2}) (-?\d+)'
    )

    COMPARATORS = {
        '<': operator.lt,
        '>': operator.gt,
        '==': operator.eq,
        '!=': operator.ne,
        '<=': operator.le,
        '>=': operator.ge
    }

    def __init__(self, instruction):
        match = self.REGEX.match(instruction)
        self.register = match.group(1)
        self.increase = match.group(2) == 'inc'
        self.amount = int(match.group(3))
        self.condition_register = match.group(4)
        comparator = match.group(5)
        value = int(match.group(6))
        self.condition = lambda x: self.COMPARATORS[comparator](x, value)

    def execute(self, memory):
        if self.is_condition_satisfied(memory):
            if self.increase:
                memory[self.register] += self.amount
            else:
                memory[self.register] -= self.amount

    def is_condition_satisfied(self, memory):
        return self.condition(memory[self.condition_register])


class Program:

    def __init__(self, instructions):
        self.instructions = instructions
        self.highest_after = 0
        self.highest_during = 0

    def execute(self):
        memory = defaultdict(int)
        for i in self.instructions:
            i.execute(memory)
            self.highest_during = max(self.highest_during, memory[i.register])
        self.highest_after = max(memory.values())


class Day08(Day):

    def __init__(self, program):
        instructions = [i for i in program.splitlines()]
        self.program = Program([Instruction(i) for i in instructions])
        self.program.execute()

    def solve_part_one(self):
        return self.program.highest_after

    def solve_part_two(self):
        return self.program.highest_during
