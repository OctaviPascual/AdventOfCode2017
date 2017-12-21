from day import Day


class Captcha:

    def __init__(self, sequence):
        self.seq = sequence
        self.offset_next = self.solve(1)
        self.offset_halfway = self.solve(len(sequence) // 2)

    def solve(self, offset):
        result = 0
        shifted_seq = self.seq[offset:] + self.seq[:offset]
        for current_digit, next_digit in zip(self.seq, shifted_seq):
            if current_digit == next_digit:
                result += int(current_digit)
        return result


class Day01(Day):

    def __init__(self, sequence):
        self.captcha = Captcha(sequence)

    def solve_part_one(self):
        return self.captcha.offset_next

    def solve_part_two(self):
        return self.captcha.offset_halfway
