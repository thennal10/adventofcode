from math import gcd
from itertools import permutations

class Moon:
    def __init__(self, position):
        self.pos = position
        self.vel = [0, 0, 0]

    def apply_vel(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[2] += self.vel[2]

    def calc_energy(self):
        potential = abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
        kinetic = abs(self.vel[0]) + abs(self.vel[1]) + abs(self.vel[2])
        return potential * kinetic


moons = [Moon([3, 2, -6]),
         Moon([-13, 18, 10]),
         Moon([-8, -1, 13]),
         Moon([5, 10, 4])]


timesteps = [0, 0, 0]

for c in range(3):
    initial = [m.pos[c] for m in moons]
    while True:
        timesteps[c] += 1
        for m in permutations(moons, 2):
            if m[0].pos[c] > m[1].pos[c]:
                m[0].vel[c] -= 1
                m[1].vel[c] += 1
        for moon in moons:
            moon.apply_vel()
        if [m.pos[c] for m in moons] == initial:
            timesteps[c] += 1
            break

print(timesteps)
lcm = timesteps[0]
for i in timesteps[1:]:
  lcm = lcm*i//gcd(lcm, i)

print(lcm)