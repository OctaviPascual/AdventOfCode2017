from functools import reduce
from day import Day


class Image:

    def __init__(self, pixels):
        self.pixels = pixels
        self.height = len(pixels)
        self.width = len(pixels[0])

    def __eq__(self, other):
        return self.pixels == other.pixels

    def __hash__(self):
        # Pretty awkward way to hash, but for this problem it works and is simple
        return hash(repr(self.pixels))

    def rotate(self):
        # Totally stolen from: https://stackoverflow.com/q/8421337
        return Image(list(map(list, zip(*self.pixels[::-1]))))

    def flip(self):
        return Image(self.pixels[::-1])

    def pixels_on(self):
        return sum([row.count('#') for row in self.pixels])

    def matching_patterns(self):
        return [
            self,
            self.flip(),
            self.flip().rotate(),
            self.flip().rotate().rotate(),
            self.flip().rotate().rotate().rotate(),
            self.rotate(),
            self.rotate().rotate(),
            self.rotate().rotate().rotate()
        ]

    def square_2x2(self, i, j):
        return Image([
            [self.pixels[i][j],   self.pixels[i][j+1]  ],
            [self.pixels[i+1][j], self.pixels[i+1][j+1]]
        ])

    def square_3x3(self, i, j):
        return Image([
            [self.pixels[i][j],   self.pixels[i][j+1],   self.pixels[i][j+2]  ],
            [self.pixels[i+1][j], self.pixels[i+1][j+1], self.pixels[i+1][j+2]],
            [self.pixels[i+2][j], self.pixels[i+2][j+1], self.pixels[i+2][j+2]]
        ])

    def merge_horizontally(self, image):
        if len(self.pixels) != len(image.pixels):
            raise ValueError('Both images must have the same horizontal size')

        merged_pixels = []
        for row1, row2 in zip(self.pixels, image.pixels):
            merged_pixels.append(row1 + row2)
        return Image(merged_pixels)

    def merge_vertically(self, image):
        if len(self.pixels[0]) != len(image.pixels[0]):
            raise ValueError('Both images must have the same vertical size')

        return Image(self.pixels + image.pixels)


class ArtGenerator:

    def __init__(self, rules, iterations):
        self.iterations = iterations
        self.image = Image([
            ['.', '#', '.'],
            ['.', '.', '#'],
            ['#', '#', '#']
        ])
        self.rules = {}
        self.build_rules(rules)
        self.generate()

    def build_image(self, image):
        return Image([list(row) for row in image.split('/')])

    def build_rules(self, rules):
        for rule in rules:
            input  = self.build_image(rule.split(' => ')[0])
            output = self.build_image(rule.split(' => ')[1])
            # Add all the matching inputs in the rules so to apply a rule
            # we only have to lookup the rules dict
            # That way we do not have to call matching_patterns() each time
            # we try to apply a rule
            for pattern in input.matching_patterns():
                self.rules[pattern] = output

    def apply_rule(self, square):
        if square not in self.rules:
            raise AssertionError('Could not find a matching rule')
        return self.rules[square]

    def enhance(self, square_size, square_nxn):
        full_image = []
        for i in range(0, self.image.height, square_size):
            squares = []
            for j in range(0, self.image.width, square_size):
                enhanced_square = square_nxn(self.image, i, j)
                squares.append(self.apply_rule(enhanced_square))
            # squares is a list of images [Image1, .., ImageN] and we have
            # to merge them horizontally to obtain a partial_image
            partial_image = reduce(lambda x, y: x.merge_horizontally(y), squares)
            full_image.append(partial_image)
        # full_image is a list of images [Image1, .., ImageN] and we have
        # to merge them vertically to obtain the final enhanced image
        self.image = reduce(lambda x, y: x.merge_vertically(y), full_image)

    def generate(self):
        for _ in range(self.iterations):
            if self.image.height % 2 == 0:
                self.enhance(2, Image.square_2x2)
            else:
                self.enhance(3, Image.square_3x3)
            # The image must always be squared after each enhancement
            assert self.image.height == self.image.width


class Day21(Day):

    def __init__(self, rules, iterations=None):
        self.rules = rules.splitlines()
        self.iterations = iterations

    def solve_part_one(self):
        iterations = 5 if self.iterations is None else self.iterations
        art_generator = ArtGenerator(self.rules, iterations)
        return art_generator.image.pixels_on()

    def solve_part_two(self):
        iterations = 18 if self.iterations is None else self.iterations
        art_generator = ArtGenerator(self.rules, iterations)
        return art_generator.image.pixels_on()
