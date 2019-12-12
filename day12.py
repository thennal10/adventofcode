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


timesteps = 1000
for step in range(timesteps):
    for m in permutations(moons, 2):
        if m[0].pos[0] > m[1].pos[0]:
            m[0].vel[0] -= 1
            m[1].vel[0] += 1
        if m[0].pos[1] > m[1].pos[1]:
            m[0].vel[1] -= 1
            m[1].vel[1] += 1
        if m[0].pos[2] > m[1].pos[2]:
            m[0].vel[2] -= 1
            m[1].vel[2] += 1
    for moon in moons:
        moon.apply_vel()

energy = 0
for moon in moons:
    energy += moon.calc_energy()

print(energy)