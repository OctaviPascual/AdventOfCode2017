import argparse
import unittest
from day01.day01 import Day01
from day02.day02 import Day02
from day03.day03 import Day03
from day04.day04 import Day04
from day05.day05 import Day05
from day06.day06 import Day06
from day07.day07 import Day07
from day08.day08 import Day08
from day09.day09 import Day09
from day10.day10 import Day10
from day11.day11 import Day11
from day12.day12 import Day12
from day13.day13 import Day13
from day14.day14 import Day14
from day15.day15 import Day15
from day16.day16 import Day16
from day17.day17 import Day17
from day18.day18 import Day18
from day19.day19 import Day19
from day20.day20 import Day20
from day21.day21 import Day21
from day22.day22 import Day22
from day23.day23 import Day23

CALENDAR = {
    1:  {'class': Day01, 'path': './day01'},
    2:  {'class': Day02, 'path': './day02'},
    3:  {'class': Day03, 'path': './day03'},
    4:  {'class': Day04, 'path': './day04'},
    5:  {'class': Day05, 'path': './day05'},
    6:  {'class': Day06, 'path': './day06'},
    7:  {'class': Day07, 'path': './day07'},
    8:  {'class': Day08, 'path': './day08'},
    9:  {'class': Day09, 'path': './day09'},
    10: {'class': Day10, 'path': './day10'},
    11: {'class': Day11, 'path': './day11'},
    12: {'class': Day12, 'path': './day12'},
    13: {'class': Day13, 'path': './day13'},
    14: {'class': Day14, 'path': './day14'},
    15: {'class': Day15, 'path': './day15'},
    16: {'class': Day16, 'path': './day16'},
    17: {'class': Day17, 'path': './day17'},
    18: {'class': Day18, 'path': './day18'},
    19: {'class': Day19, 'path': './day19'},
    20: {'class': Day20, 'path': './day20'},
    21: {'class': Day21, 'path': './day21'},
    22: {'class': Day22, 'path': './day22'},
    23: {'class': Day23, 'path': './day23'}
}


def check_day(string):
    day = int(string)
    if 1 <= day <= 25:
        return day
    raise argparse.ArgumentTypeError("Invalid day (must be in [1..25] range)")


def run_day(i):
    print('********************************')
    print('************ Day {:2d} ************'.format(i))
    print('********************************')

    day_dict = CALENDAR[i]
    input = day_dict['path'] + '/input.txt'
    day = day_dict['class'](open(input).read())
    print('- Part One: ' + str(day.solve_part_one()))
    print('- Part Two: ' + str(day.solve_part_two()))
    print('********************************')
    print()
    print("Running unit tests:")
    run_test(day_dict['path'])


def run_test(path):
    loader = unittest.TestLoader()
    suite = loader.discover(path)

    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(suite)


def main():
    parser = argparse.ArgumentParser(description='Run Advent of Code 2017')
    parser.add_argument('-d', '--day',
                        help='day to run (all by default)',
                        type=check_day)
    args = parser.parse_args()

    print()
    print('--------------------------------')
    print('----- Advent of Code 2017 ------')
    print('--------------------------------')
    print()

    if args.day is None:
        list(map(run_day, CALENDAR))
    else:
        run_day(args.day)


if __name__ == '__main__':
    main()
