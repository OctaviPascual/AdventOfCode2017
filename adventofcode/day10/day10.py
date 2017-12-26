from collections import deque
from functools import reduce
from day import Day


class KnotHashBase:

    def __init__(self, lengths, size):
        self.lengths = lengths
        self.skip_size = 0
        self.total_rotations = 0
        self.hash = deque(range(size))

    # Instead of a straightforward implementation of the algorithm,
    # rotations are performed on the list so wrapping around to the front
    # when reaching the end is not needed, that simplifies the process.
    # To obtain original's algorithm result, rotations must be undone.
    def round(self, last=True):
        for length in self.lengths:
            self.reverse(length)
            self.move(length)
            self.skip_size += 1
        # Undo all rotations by rotating to the right
        if last:
            self.hash.rotate(self.total_rotations)

    def reverse(self, length):
        aux = list(self.hash)
        self.hash = deque(aux[:length][::-1] + aux[length:])

    def move(self, length):
        rotation = self.skip_size + length
        # Rotate to the left to emulate moving index to the right
        self.hash.rotate(-rotation)
        self.total_rotations += rotation


class KnotHash(KnotHashBase):

    ROUNDS = 64
    SUFFIX = [17, 31, 73, 47, 23]
    CHUNK_SIZE = 16

    def __init__(self, lengths, size=256):
        self.dense_hash = None
        lengths = [ord(l) for l in lengths]
        super().__init__(lengths + KnotHash.SUFFIX, size)

    def execute(self):
        for _ in range(KnotHash.ROUNDS - 1):
            self.round(False)
        self.round(last=True)

        sparse_hash = list(self.hash)
        self.compute_dense_hash(sparse_hash, KnotHash.CHUNK_SIZE)
        self.hash = ''.join(list(map(lambda x: '{:02x}'.format(x), self.dense_hash)))

    def compute_dense_hash(self, l, n):
        # Stolen from https://stackoverflow.com/a/312464
        chunks = [l[i:i + n] for i in range(0, len(l), n)]
        self.dense_hash = [reduce(lambda x, y: x ^ y, c) for c in chunks]


class Day10(Day):

    def __init__(self, lengths, size=256):
        self.lengths = lengths
        self.size = size

    def solve_part_one(self):
        lengths = [int(l) for l in self.lengths.split(',')]
        knot_hash_base = KnotHashBase(lengths, self.size)
        knot_hash_base.round()
        return knot_hash_base.hash[0] * knot_hash_base.hash[1]

    def solve_part_two(self):
        knot_hash = KnotHash(self.lengths, self.size)
        knot_hash.execute()
        return knot_hash.hash
