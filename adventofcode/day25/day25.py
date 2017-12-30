import re
from collections import defaultdict
from day import Day


class Rule:

    def __init__(self, write, move, next_state):
        self.write_value = write
        self.move_direction = move
        self.next_state = next_state

    def execute(self, turing_machine):
        turing_machine.write(self.write_value)
        turing_machine.move(self.move_direction)
        turing_machine.set_state(self.next_state)


class State:

    REGEX = re.compile(
        r''
        r'In state (\w):'
        r'  If the current value is 0:'
        r'    - Write the value (\d).'
        r'    - Move one slot to the (\bleft\b|\bright\b).'
        r'    - Continue with state (\w).'
        r'  If the current value is 1:'
        r'    - Write the value (\d).'
        r'    - Move one slot to the (\bleft\b|\bright\b).'
        r'    - Continue with state (\w).'
    )

    def __init__(self, blueprint):
        match = State.REGEX.match(blueprint)

        self.label = match.group(1)

        write = int(match.group(2))
        move = match.group(3)
        next_state = match.group(4)
        rule_0 = Rule(write, move, next_state)

        write = int(match.group(5))
        move = match.group(6)
        next_state = match.group(7)
        rule_1 = Rule(write, move, next_state)

        self.rules = {
            0: rule_0,
            1: rule_1
        }

    def execute(self, turing_machine):
        value = turing_machine.current_value()
        self.rules[value].execute(turing_machine)


class TuringMachine:

    REGEX = re.compile(
        r'Begin in state (\w).'
        r'Perform a diagnostic checksum after (\d+) steps.'
    )

    def __init__(self, blueprint):
        self.tape = defaultdict(int)
        self.cursor = 0
        self.state = None
        self.steps = None
        self.states = {}
        self.build(blueprint)
        self.execute()

    def build(self, blueprint):
        match = TuringMachine.REGEX.match(''.join(blueprint[:2]))
        self.state = match.group(1)
        self.steps = int(match.group(2))

        for i in range(2, len(blueprint), 10):
            state = State(''.join(blueprint[i:i+10]))
            self.states[state.label] = state

    def execute(self):
        for _ in range(self.steps):
            self.states[self.state].execute(self)

    def current_value(self):
        return self.tape[self.cursor]

    def write(self, value):
        self.tape[self.cursor] = value

    def move(self, direction):
        if direction == 'left':
            self.cursor -= 1
        elif direction == 'right':
            self.cursor += 1
        else:
            raise ValueError('The cursor can only be moved left or right')

    def set_state(self, state):
        self.state = state

    def diagnostic_checksum(self):
        return list(self.tape.values()).count(1)


class Day25(Day):

    def __init__(self, blueprint):
        self.turing_machine = TuringMachine(blueprint.splitlines())

    def solve_part_one(self):
        return self.turing_machine.diagnostic_checksum()

    def solve_part_two(self):
        # There was no part two for the final puzzle!
        pass
