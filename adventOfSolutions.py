from day1.captcha import Captcha
from day2.checksum import Checksum
from day3.memory import Memory
from day4.passphrase import Passphrase
from day5.maze import Maze
from day6.reallocation import Reallocation
from day7.day7 import Day7
from day8.day8 import Day8
from day9.day9 import Day9

print('***************')
print('**** Day 1 ****')
print('***************')
captcha = Captcha(open('./day1/input.txt').read())
print('- Part One: ' + str(captcha.solve_part_one()))
print('- Part Two: ' + str(captcha.solve_part_two()))

print('***************')
print('**** Day 2 ****')
print('***************')
checksum = Checksum(open('./day2/input.txt').read())
print('- Part One: ' + str(checksum.solve_part_one()))
print('- Part Two: ' + str(checksum.solve_part_two()))

print('***************')
print('**** Day 3 ****')
print('***************')
memory = Memory(open('./day3/input.txt').read())
print('- Part One: ' + str(memory.solve_part_one()))
print('- Part Two: ' + str(memory.solve_part_two()))

print('***************')
print('**** Day 4 ****')
print('***************')
memory = Passphrase(open('./day4/input.txt').read())
print('- Part One: ' + str(memory.solve_part_one()))
print('- Part Two: ' + str(memory.solve_part_two()))

print('***************')
print('**** Day 5 ****')
print('***************')
maze = Maze(open('./day5/input.txt').read())
print('- Part One: ' + str(maze.solve_part_one()))
#print('- Part Two: ' + str(maze.solve_part_two()))

print('***************')
print('**** Day 6 ****')
print('***************')
reallocation = Reallocation(open('./day6/input.txt').read())
print('- Part One: ' + str(reallocation.solve_part_one()))
print('- Part Two: ' + str(reallocation.solve_part_two()))

print('***************')
print('**** Day 7 ****')
print('***************')
day7 = Day7(open('./day7/input.txt').read())
print('- Part One: ' + str(day7.solve_part_one()))
print('- Part Two: ' + str(day7.solve_part_two()))

print('***************')
print('**** Day 8 ****')
print('***************')
day8 = Day8(open('./day8/input.txt').read())
print('- Part One: ' + str(day8.solve_part_one()))
print('- Part Two: ' + str(day8.solve_part_two()))


print('***************')
print('**** Day 9 ****')
print('***************')
day9 = Day9(open('./day9/input.txt').read())
print('- Part One: ' + str(day9.solve_part_one()))
print('- Part Two: ' + str(day9.solve_part_two()))
