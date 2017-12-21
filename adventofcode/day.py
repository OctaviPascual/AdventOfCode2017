from abc import ABC, abstractmethod


class Day(ABC):

    @abstractmethod
    def solve_part_one(self):
        return NotImplementedError

    @abstractmethod
    def solve_part_two(self):
        return NotImplementedError
