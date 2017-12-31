# Advent of Code 2017

My solutions for [Advent of Code 2017](https://adventofcode.com/2017) in [Python](https://www.python.org/).

Special thanks to [Erisc Wastl](http://was.tl) and the rest of the [AoC team](https://adventofcode.com/2017/about) for such an awesome set of challenges! :bowtie:

* **[Day  1: Inverse Captcha][day01]** *([code][code01])*
* **[Day  2: Corruption Checksum][day02]** *([code][code02])*
* **[Day  3: Spiral Memory][day03]** *([code][code03])*
* **[Day  4: High-Entropy Passphrases][day04]** *([code][code04])*
* **[Day  5: A Maze of Twisty Trampolines, All Alike][day05]** *([code][code05])*
* **[Day  6: Memory Reallocation][day06]** *([code][code06])*
* **[Day  7: Recursive Circus][day07]** *([code][code07])*
* **[Day  8: I Heard You Like Registers][day08]** *([code][code08])*
* **[Day  9: Stream Processing][day09]** *([code][code09])*
* **[Day 10: Knot Hash][day10]** *([code][code10])*
* **[Day 11: Hex Ed][day11]** *([code][code11])*
* **[Day 12: Digital Plumber][day12]** *([code][code12])*
* **[Day 13: Packet Scanners][day13]** *([code][code13])*
* **[Day 14: Disk Defragmentation][day14]** *([code][code14])*
* **[Day 15: Dueling Generators][day15]** *([code][code15])*
* **[Day 16: Permutation Promenade][day16]** *([code][code16])*
* **[Day 17: Spinlock][day17]** *([code][code17])*
* **[Day 18: Duet][day18]** *([code][code18])*
* **[Day 19: A Series of Tubes][day19]** *([code][code19])*
* **[Day 20: Particle Swarm][day20]** *([code][code20])*
* **[Day 21: Fractal Art][day21]** *([code][code21])*
* **[Day 22: Sporifica Virus][day22]** *([code][code22])*
* **[Day 23: Coprocessor Conflagration][day23]** *([code][code23])* *([image](docs/pseudocode.jpeg))*
* **[Day 24: Electromagnetic Moat][day24]** *([code][code24])*
* **[Day 25: The Halting Problem][day25]** *([code][code25])*

[day01]: https://adventofcode.com/2017/day/1
[day02]: https://adventofcode.com/2017/day/2
[day03]: https://adventofcode.com/2017/day/3
[day04]: https://adventofcode.com/2017/day/4
[day05]: https://adventofcode.com/2017/day/5
[day06]: https://adventofcode.com/2017/day/6
[day07]: https://adventofcode.com/2017/day/7
[day08]: https://adventofcode.com/2017/day/8
[day09]: https://adventofcode.com/2017/day/9
[day10]: https://adventofcode.com/2017/day/10
[day11]: https://adventofcode.com/2017/day/11
[day12]: https://adventofcode.com/2017/day/12
[day13]: https://adventofcode.com/2017/day/13
[day14]: https://adventofcode.com/2017/day/14
[day15]: https://adventofcode.com/2017/day/15
[day16]: https://adventofcode.com/2017/day/16
[day17]: https://adventofcode.com/2017/day/17
[day18]: https://adventofcode.com/2017/day/18
[day19]: https://adventofcode.com/2017/day/19
[day20]: https://adventofcode.com/2017/day/20
[day21]: https://adventofcode.com/2017/day/21
[day22]: https://adventofcode.com/2017/day/22
[day23]: https://adventofcode.com/2017/day/23
[day24]: https://adventofcode.com/2017/day/24
[day25]: https://adventofcode.com/2017/day/25

[code01]: adventofcode/day01/day01.py
[code02]: adventofcode/day02/day02.py
[code03]: adventofcode/day03/day03.py
[code04]: adventofcode/day04/day04.py
[code05]: adventofcode/day05/day05.py
[code06]: adventofcode/day06/day06.py
[code07]: adventofcode/day07/day07.py
[code08]: adventofcode/day08/day08.py
[code09]: adventofcode/day09/day09.py
[code10]: adventofcode/day10/day10.py
[code11]: adventofcode/day11/day11.py
[code12]: adventofcode/day12/day12.py
[code13]: adventofcode/day13/day13.py
[code14]: adventofcode/day14/day14.py
[code15]: adventofcode/day15/day15.py
[code16]: adventofcode/day16/day16.py
[code17]: adventofcode/day17/day17.py
[code18]: adventofcode/day18/day18.py
[code19]: adventofcode/day19/day19.py
[code20]: adventofcode/day20/day20.py
[code21]: adventofcode/day21/day21.py
[code22]: adventofcode/day22/day22.py
[code23]: adventofcode/day23/day23.py
[code24]: adventofcode/day24/day24.py
[code25]: adventofcode/day25/day25.py

## Usage

The main program of this project is [adventofcode.py](adventofcode/adventofcode.py). You must use this program to run any day puzzle. Usage is pretty straightforward. Note that DAY can be any number from 1 to 25. You can find a sample of the ouput in [output.txt](docs/output.txt).

```text
usage: adventofcode.py [-h] [-d DAY]

Run Advent of Code 2017

optional arguments:
  -h, --help         show this help message and exit
  -d DAY, --day DAY  day to run (all by default)
```

I only used built-in modules, so it should be easy to run the program in your local machine. Just note that [Python3](https://www.python.org/downloads/) is required. However, to ensure that indeed the program works, I have [dockerized](#docker) the program.

#### Run all days

```bash
git clone https://github.com/EikaNN/AdventOfCode2017.git
cd AdventOfCode2017/adventofcode
python adventofcode.py
```

#### Run a specific day

```bash
git clone https://github.com/EikaNN/AdventOfCode2017.git
cd AdventOfCode2017/adventofcode
python adventofcode.py -d DAY
```

## Docker

If you want to use [Docker](https://www.docker.com/get-docker), there are two docker images available. The first one uses [Python](https://www.python.org/) while the second one uses [PyPy](https://pypy.org/), which speeds up considerably the execution.

The following table shows how much it takes to run all days in both Python and Pypy, and the performance gain is substantial, especially considering that no source code modifications were needed!

| Python  | PyPy    |
|---------|---------|
| 9min44s | 1min20s |

### Python

#### Run a specific day

```bash
git clone https://github.com/EikaNN/AdventOfCode2017.git
cd AdventOfCode2017/docker
./docker_python.sh -d DAY
```

#### Run all days

```bash
git clone https://github.com/EikaNN/AdventOfCode2017.git
cd AdventOfCode2017/docker
./docker_python.sh
```

### PyPy

#### Run a specific day

```bash
git clone https://github.com/EikaNN/AdventOfCode2017.git
cd AdventOfCode2017/docker
./docker_pypy.sh -d DAY
```

#### Run all days

```bash
git clone https://github.com/EikaNN/AdventOfCode2017.git
cd AdventOfCode2017/docker
./docker_pypy.sh
```
