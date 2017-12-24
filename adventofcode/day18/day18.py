import re
import operator
from collections import defaultdict
from day import Day


class Instruction:

    SND = r'snd ([a-z]|\-?\d+)'
    SET = r'set ([a-z]) ([a-z]|\-?\d+)'
    ADD = r'add ([a-z]) ([a-z]|\-?\d+)'
    MUL = r'mul ([a-z]) ([a-z]|\-?\d+)'
    MOD = r'mod ([a-z]) ([a-z]|\-?\d+)'
    RCV = r'rcv ([a-z]|\-?\d+)'
    JGZ = r'jgz ([a-z]|\-?\d+) ([a-z]|\-?\d+)'

    def __init__(self, instruction):
        self.instruction = instruction

    def execute(self, memory):
        snd = re.match(Instruction.SND, self.instruction)
        set = re.match(Instruction.SET, self.instruction)
        add = re.match(Instruction.ADD, self.instruction)
        mul = re.match(Instruction.MUL, self.instruction)
        mod = re.match(Instruction.MOD, self.instruction)
        rcv = re.match(Instruction.RCV, self.instruction)
        jgz = re.match(Instruction.JGZ, self.instruction)

        if snd:
            x = snd.group(1)
            Instruction.snd(x, memory)
        elif set:
            x = set.group(1)
            y = set.group(2)
            Instruction.set(x, y, memory)
        elif add:
            x = add.group(1)
            y = add.group(2)
            Instruction.operate(x, y, memory, operator.add)
        elif mul:
            x = mul.group(1)
            y = mul.group(2)
            Instruction.operate(x, y, memory, operator.mul)
        elif mod:
            x = mod.group(1)
            y = mod.group(2)
            Instruction.operate(x, y, memory, operator.mod)
        elif rcv:
            x = rcv.group(1)
            Instruction.rcv(x, memory)
        elif jgz:
            x = jgz.group(1)
            y = jgz.group(2)
            Instruction.jgz(x, y, memory)
        else:
            i = '"' + self.instruction + '"'
            raise SyntaxError('The following instruction is invalid: ' + i)

        memory['program_counter'] += 1

    @staticmethod
    def get_argument(x, memory):
        # isdigit does not match negative numbers, so we remove the minus sign
        return int(x) if x.lstrip('-').isdigit() else memory['registers'][x]

    @staticmethod
    def snd(x, memory):
        x = Instruction.get_argument(x, memory)
        memory['sounds'].append(x)

    @staticmethod
    def set(x, y, memory):
        y = Instruction.get_argument(y, memory)
        memory['registers'][x] = y

    @staticmethod
    def operate(x, y, memory, op):
        y = Instruction.get_argument(y, memory)
        registers = memory['registers']
        registers[x] = op(registers[x], y)

    @staticmethod
    def rcv(x, memory):
        x = Instruction.get_argument(x, memory)
        if x != 0:
            memory['recover'] = memory['sounds'][-1]
            # Ensure program will end right after this instruction
            memory['program_counter'] = -2

    @staticmethod
    def jgz(x, y, memory):
        x = Instruction.get_argument(x, memory)
        y = Instruction.get_argument(y, memory)
        if x > 0:
            # Since program_counter is always incremented by one
            # we need to take one from the offset y
            memory['program_counter'] += y-1


class Solo:

    def __init__(self, instructions):
        self.instructions = instructions
        self.memory = {
            'program_counter': 0,
            'registers': defaultdict(int),
            'sounds': [],
            'recover': None
        }

    def execute(self):
        while True:
            pc = self.memory['program_counter']
            if 0 <= pc < len(self.instructions):
                self.instructions[pc].execute(self.memory)
            else:
                break
        return self.memory


class Day18(Day):

    def __init__(self, program):
        program = [Instruction(i) for i in program.split('\n')]
        self.solo = Solo(program)

    def solve_part_one(self):
        self.solo.execute()
        return self.solo.memory['recover']

    def solve_part_two(self):
        pass
