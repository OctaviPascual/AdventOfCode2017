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
            self.snd(x, memory)
        elif set:
            x = set.group(1)
            y = set.group(2)
            self.set(x, y, memory)
        elif add:
            x = add.group(1)
            y = add.group(2)
            self.operate(x, y, memory, operator.add)
        elif mul:
            x = mul.group(1)
            y = mul.group(2)
            self.operate(x, y, memory, operator.mul)
        elif mod:
            x = mod.group(1)
            y = mod.group(2)
            self.operate(x, y, memory, operator.mod)
        elif rcv:
            x = rcv.group(1)
            self.rcv(x, memory)
        elif jgz:
            x = jgz.group(1)
            y = jgz.group(2)
            self.jgz(x, y, memory)
        else:
            i = '"' + self.instruction + '"'
            raise SyntaxError('The following instruction is invalid: ' + i)

        memory['program_counter'] += 1

    @staticmethod
    def get_value(arg, memory):
        return memory['registers'][arg] if arg.isalpha() else int(arg)

    @staticmethod
    def snd(x, memory):
        x = Instruction.get_value(x, memory)
        memory['sound'] = x

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
    def rcv(x, memory):
        x = Instruction.get_value(x, memory)
        if x != 0:
            memory['recover'] = memory['sound']
            # Ensure program will end right after this instruction
            memory['program_counter'] = -2

    @staticmethod
    def jgz(x, y, memory):
        x = Instruction.get_value(x, memory)
        y = Instruction.get_value(y, memory)
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
            'sound': None,
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


# We need to override two instructions for part 2
class InstructionDuet(Instruction):

    @staticmethod
    def snd(x, memory):
        x = Instruction.get_value(x, memory)
        assert memory['send'] is None
        memory['send'] = x

    @staticmethod
    def rcv(x, memory):
        if not memory['receive']:
            # We must wait so we execute the same instruction again
            memory['program_counter'] -= 1
        else:
            memory['registers'][x] = memory['receive'].pop(0)


class Duet:

    def __init__(self, instructions):
        self.instructions = instructions
        self.memory_0 = {
            'program_counter': 0,
            'registers': defaultdict(int),
            'send': None,
            'receive': [],
            'count': 0
        }
        self.memory_1 = {
            'program_counter': 0,
            'registers': defaultdict(int),
            'send': None,
            'receive': [],
            'count': 0
        }
        self.memory_0['registers']['p'] = 0
        self.memory_1['registers']['p'] = 1

    def execute(self):

        while True:
            pc_0 = self.memory_0['program_counter']
            pc_1 = self.memory_1['program_counter']

            if 0 <= pc_0 < len(self.instructions):
                self.instructions[pc_0].execute(self.memory_0)

            if 0 <= pc_1 < len(self.instructions):
                self.instructions[pc_1].execute(self.memory_1)

            send_0 = self.memory_0['send']
            if send_0 is not None:
                self.memory_1['receive'].append(send_0)
                self.memory_0['count'] += 1
                self.memory_0['send'] = None

            send_1 = self.memory_1['send']
            if send_1 is not None:
                self.memory_0['receive'].append(send_1)
                self.memory_1['count'] += 1
                self.memory_1['send'] = None

            # Detect if we have reached a deadlock
            wait_0 = pc_0 == self.memory_0['program_counter']
            wait_1 = pc_1 == self.memory_1['program_counter']
            if wait_0 and wait_1:
                break


class Day18(Day):

    def __init__(self, program):
        self.program = program.splitlines()

    def solve_part_one(self):
        solo = Solo([Instruction(i) for i in self.program])
        solo.execute()
        return solo.memory['recover']

    def solve_part_two(self):
        duet = Duet([InstructionDuet(i) for i in self.program])
        duet.execute()
        return duet.memory_1['count']
