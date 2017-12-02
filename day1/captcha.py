class Captcha:

    def __init__(self, captcha):
        self.captcha = captcha

    def solve(self, offset):
        result = 0
        shifted_captcha = self.captcha[offset:] + self.captcha[:offset]
        for current_digit,next_digit in zip(self.captcha, shifted_captcha):
            if current_digit == next_digit: result += int(current_digit)
        return result

    def solve_part_one(self):
        return self.solve(1)

    def solve_part_two(self):
        return self.solve(len(self.captcha) // 2)
