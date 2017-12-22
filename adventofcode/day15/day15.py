from day import Day


class Generator:

    MOD = 2147483647

    def __init__(self, factor, starting_value, multiple=1):
        self.factor = factor
        self.value = starting_value
        self.multiple = multiple

    # Good excuse to learn and use yield
    # https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
    def generate(self):
        while True:
            self.value = self.value*self.factor % Generator.MOD
            while self.value % self.multiple != 0:
                self.value = self.value*self.factor % Generator.MOD
            yield self.value


class Judge:

    FACTOR_A = 16807
    FACTOR_B = 48271

    MULTIPLE_A = 4
    MULTIPLE_B = 8

    def __init__(self, start_a, start_b, rounds, picky_generators=False):
        self.rounds = rounds
        if picky_generators:
            self.generator_a = Generator(Judge.FACTOR_A,
                                         start_a,
                                         Judge.MULTIPLE_A).generate()
            self.generator_b = Generator(Judge.FACTOR_B,
                                         start_b,
                                         Judge.MULTIPLE_B).generate()
        else:
            self.generator_a = Generator(Judge.FACTOR_A, start_a).generate()
            self.generator_b = Generator(Judge.FACTOR_B, start_b).generate()

    def execute(self):
        matching_pairs = 0
        for i in range(self.rounds):
            a = next(self.generator_a)
            b = next(self.generator_b)
            if Judge.lowest_16_bits(a) == Judge.lowest_16_bits(b):
                matching_pairs += 1
        return matching_pairs

    @staticmethod
    def lowest_16_bits(n):
        return n & 0xFFFF


class Day15(Day):

    def __init__(self, starts):
        self.start_a = int(starts.split('\n')[0].split()[-1])
        self.start_b = int(starts.split('\n')[1].split()[-1])

    def solve_part_one(self):
        return Judge(self.start_a, self.start_b, 40 * 10**6).execute()

    def solve_part_two(self):
        return Judge(self.start_a, self.start_b, 5 * 10**6, True).execute()
