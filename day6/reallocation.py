class MemoryBanks:

    def __init__(self, banks):
        self.banks = tuple(banks)

    def __eq__(self, other):
        return self.banks == other.banks

    def __hash__(self):
        return hash(self.banks)

    def get_bank_with_most_blocks(self):
        return self.banks.index(max(self.banks))

    def redistribute(self):

        i = self.get_bank_with_most_blocks()
        n = len(self.banks)
        redistributed_banks = list(self.banks)
        blocks = redistributed_banks[i]
        redistributed_banks[i] = 0

        while blocks > 0:
            blocks -= 1
            i += 1
            redistributed_banks[i%n] += 1

        return MemoryBanks(redistributed_banks)


class Reallocation:

    def __init__(self, blocks):
        self.blocks = [int(x) for x in blocks.split()]

    def solve_part_one(self):

        memory_banks = MemoryBanks(self.blocks)
        redistributions = 0
        states = {memory_banks}

        while True:
            memory_banks = memory_banks.redistribute()
            redistributions += 1
            if memory_banks in states:
                return redistributions
            states.add(memory_banks)

    def solve_part_two(self):

        memory_banks = MemoryBanks(self.blocks)
        redistributions = 0
        states = {memory_banks: redistributions}

        while True:
            memory_banks = memory_banks.redistribute()
            redistributions += 1
            if memory_banks in states:
                return redistributions - states[memory_banks]
            states[memory_banks] = redistributions
