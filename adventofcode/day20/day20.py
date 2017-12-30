import re
import math
from collections import namedtuple, defaultdict
from day import Day


class Particle:

    REGEX = re.compile(
        r'p=<(-?\d+),(-?\d+),(-?\d+)>, '
        r'v=<(-?\d+),(-?\d+),(-?\d+)>, '
        r'a=<(-?\d+),(-?\d+),(-?\d+)>'
    )

    Position = namedtuple('Position', ['x', 'y', 'z'])
    Velocity = namedtuple('Velocity', ['x', 'y', 'z'])
    Acceleration = namedtuple('Acceleration', ['x', 'y', 'z'])

    def __init__(self, particle):
        m = Particle.REGEX.match(particle)
        l = list(map(int, list(m.groups())))
        self.position = Particle.Position(l[0], l[1], l[2])
        self.velocity = Particle.Velocity(l[3], l[4], l[5])
        self.acceleration = Particle.Acceleration(l[6], l[7], l[8])

    @staticmethod
    def origin():
        return Particle('p=<0,0,0>, v=<0,0,0>, a=<0,0,0>')

    def distance(self, particle):
        p1 = self.position
        p2 = particle.position
        return abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)

    def update(self):
        x = self.velocity.x + self.acceleration.x
        y = self.velocity.y + self.acceleration.y
        z = self.velocity.z + self.acceleration.z
        self.velocity = Particle.Velocity(x, y, z)

        x = self.position.x + self.velocity.x
        y = self.position.y + self.velocity.y
        z = self.position.z + self.velocity.z
        self.position = Particle.Position(x, y, z)


class Buffer:

    def __init__(self, particles):
        self.origin = Particle.origin()
        self.particles = {id: Particle(p) for id, p in enumerate(particles)}

    # The default number of iterations is arbitrary, but in my
    # case 500 were enough to solve my puzzle input
    def simulate(self, collisions=False, iterations=500):
        for _ in range(iterations):
            for particle in self.particles.values():
                particle.update()
            if collisions:
                self.remove_colliding_particles()

    def closest_particle(self):
        closest_particle = None
        min_distance = math.inf
        for id, particle in self.particles.items():
            distance = particle.distance(self.origin)
            if distance < min_distance:
                min_distance = distance
                closest_particle = id
        return closest_particle

    def remove_colliding_particles(self):
        # Create a dict where the key is a position and the value
        # a list of particles which are in that position
        space = defaultdict(list)
        for id, particle in self.particles.items():
            space[particle.position].append(id)

        for position in space:
            # If there is more than a particle in a given position,
            # they collide so they are removed
            if len(space[position]) > 1:
                for id in space[position]:
                    del self.particles[id]


class Day20(Day):

    def __init__(self, particles):
        self.particles = particles.splitlines()

    def solve_part_one(self):
        buffer = Buffer(self.particles)
        buffer.simulate()
        return buffer.closest_particle()

    def solve_part_two(self):
        buffer = Buffer(self.particles)
        buffer.simulate(collisions=True)
        return len(buffer.particles)
