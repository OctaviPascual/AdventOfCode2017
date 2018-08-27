import re
import operator
from collections import defaultdict
from day import Day


class Instruction:

    SET = re.compile(r'set ([a-z]) ([a-z]|-?\d+)')
    SUB = re.compile(r'sub ([a-z]) ([a-z]|-?\d+)')
    MUL = re.compile(r'mul ([a-z]) ([a-z]|-?\d+)')
    JNZ = re.compile(r'jnz ([a-z]|-?\d+) ([a-z]|-?\d+)')

    def __init__(self, instruction):
        self.instruction = instruction

    def execute(self, memory):
        set = Instruction.SET.match(self.instruction)
        sub = Instruction.SUB.match(self.instruction)
        mul = Instruction.MUL.match(self.instruction)
        jnz = Instruction.JNZ.match(self.instruction)

        # Even if it incrementing the program counter before executing
        # the instruction is bizarre, it is harmless and we can
        # return which instruction has been executed right after
        # executing it, which makes the code cleaner
        memory['program_counter'] += 1

        if set:
            x = set.group(1)
            y = set.group(2)
            self.set(x, y, memory)
            return 'set'
        elif sub:
            x = sub.group(1)
            y = sub.group(2)
            self.operate(x, y, memory, operator.sub)
            return 'sub'
        elif mul:
            x = mul.group(1)
            y = mul.group(2)
            self.operate(x, y, memory, operator.mul)
            return 'mul'
        elif jnz:
            x = jnz.group(1)
            y = jnz.group(2)
            self.jnz(x, y, memory)
            return 'jnz'
        else:
            i = '"' + self.instruction + '"'
            raise SyntaxError('The following instruction is invalid: ' + i)

    @staticmethod
    def get_value(arg, memory):
        return memory['registers'][arg] if arg.isalpha() else int(arg)

    @staticmethod
    def set(x, y, memory):
        y = Instruction.get_value(y, memory)
        memory['registers'][x] = y

    @staticmethod
    def operate(x, y, memory, op):
        y = Instruction.get_value(y, memory)
        registers = memory['registers']
        registers[x] = op(registers[x], y)

    @staticmethod
    def jnz(x, y, memory):
        x = Instruction.get_value(x, memory)
        y = Instruction.get_value(y, memory)
        if x != 0:
            # Since program_counter is always incremented by one
            # we need to take one from the offset y
            memory['program_counter'] += y-1


class Program:

    def __init__(self, instructions):
        self.instructions = instructions
        self.memory = {
            'program_counter': 0,
            'registers': defaultdict(int),
            'instruction_counter': defaultdict(int)
        }

    def execute(self):
        while True:
            pc = self.memory['program_counter']
            if 0 <= pc < len(self.instructions):
                instruction = self.instructions[pc].execute(self.memory)
                self.memory['instruction_counter'][instruction] += 1
            else:
                break
        return self.memory

    # There exist more efficient ways to check if a number is prime,
    # but for this problem this was more than enough
    def is_prime(self, n):
        for i in range(2, int(n**0.5) + 1):
            if n%i == 0:
                return False
        return True

    def solve_part_two(self, b, c, step):
        h = 0
        for i in range(b, c+1, step):
            if not self.is_prime(i):
                h += 1
        return h


class Day23(Day):

    def __init__(self, program):
        self.program = program.splitlines()

    def solve_part_one(self):
        program = Program([Instruction(i) for i in self.program])
        program.execute()
        return program.memory['instruction_counter']['mul']

    def solve_part_two(self):
        # For this part, I had to translate the program to pseudocode
        # in order to figure out what it was doing

        # In the root directory of this repository, there is a img/
        # directory which contains the program said pseudocode

        # I realised that the number of iterations is 108099*108099*1000,
        # or 11685393801000, so indeed the program needed to be optimized...

        # At the end, I understood that variable h was only incremented when
        # the variable b was not a prime number, and that b took the values
        # from 108100 to 125100 with increments of 17
        # So the problem is equivalent to counting the number of composite numbers
        # in the range [108100, 125100] with step equal to 17

        # Finally, note I have hardcoded the values of b, c and step.
        # Ideally they should be retrieved from the input program, but it was not
        # straightforward at all and I did not want to dedicate more time

        b = 108100
        c = 125100
        step = 17
        return Program(None).solve_part_two(b, c, step)
