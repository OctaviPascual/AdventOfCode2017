import sys
from day import Day


class StreamProcessor:

    def __init__(self, stream):
        self.stream = stream
        self.score = 0
        self.garbage_characters = 0

    def process(self):
        self.remove_garbage()
        self.count_score(0, 0)

    def garbage_exists(self):
        return '<' in self.stream

    def next_garbage_begin(self):
        return self.stream.find('<')

    def next_garbage_end(self, i):
        if self.stream[i] == '>':
            return i
        if self.stream[i] == '!':
            # If we find a '!' we skip the next character
            return self.next_garbage_end(i+2)
        self.garbage_characters += 1
        return self.next_garbage_end(i+1)

    def remove_garbage(self):
        while self.garbage_exists():
            begin = self.next_garbage_begin()
            end = self.next_garbage_end(begin+1)
            self.stream = self.stream[:begin] + self.stream[end+1:]

    def count_score(self, i, level):
        if i < len(self.stream):
            # We start processing a group
            if self.stream[i] == '{':
                self.count_score(i+1, level+1)
            # There is another group in the same level
            if self.stream[i] == ',':
                self.count_score(i+1, level)
            # We end processing a group
            if self.stream[i] == '}':
                self.score += level
                self.count_score(i+1, level-1)


class Day09(Day):

    def __init__(self, stream):
        # We need to increase the recursion stack size
        sys.setrecursionlimit(5000)
        self.stream_processor = StreamProcessor(stream)
        self.stream_processor.process()

    def solve_part_one(self):
        return self.stream_processor.score

    def solve_part_two(self):
        return self.stream_processor.garbage_characters
