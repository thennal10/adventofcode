from itertools import permutations
from collections import Counter

pos = [int(l.split(':')[1]) - 1 for l in open('./input.txt').readlines()]

def p1(pos):
    points = [0, 0]
    d = 0
    while max(points) < 1000:
        n = (d//3) % 2
        pos[n] = (pos[n] + (3*((d % 100) + 1)) + 3) % 10
        points[n] += pos[n] + 1
        d += 3
    
    losing = min(points)
    return losing*d

print(p1(pos.copy()))

sum_to_perm = Counter()
for p in set(permutations([1]*3 + [2]*3 + [3]*3,3)):
    sum_to_perm[sum(p)] += 1

counter = Counter()
def roll(pos, die, mult, points, n=0):
    pos[n % 2] = (pos[n % 2] + die) % 10
    points[n % 2] += pos[n % 2] + 1

    if max(points) >= 21:
        counter[n % 2] += mult
        return

    for d in range(3, 10):
        roll(pos.copy(), d, sum_to_perm[d] * mult, points.copy(), n+1)

for d in range(3, 10):
    roll(pos.copy(), d, sum_to_perm[d], [0, 0])

print(counter.most_common()[0][0])

