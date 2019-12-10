from fractions import Fraction
from math import atan2

inp = """.###.#...#.#.##.#.####..
.#....#####...#.######..
#.#.###.###.#.....#.####
##.###..##..####.#.####.
###########.#######.##.#
##########.#########.##.
.#.##.########.##...###.
###.#.##.#####.#.###.###
##.#####.##..###.#.##.#.
.#.#.#####.####.#..#####
.###.#####.#..#..##.#.##
########.##.#...########
.####..##..#.###.###.#.#
....######.##.#.######.#
###.####.######.#....###
############.#.#.##.####
##...##..####.####.#..##
.###.#########.###..#.##
#.##.#.#...##...#####..#
##.#..###############.##
##.###.#####.##.######..
##.#####.#.#.##..#######
...#######.######...####
#....#.#.#.####.#.#.#.##
"""

def rat(n1, n2):
    if n1 == 0:
        return n1, n2//abs(n2)
    elif n2 == 0:
        return n1//abs(n1), n2
    fr = Fraction(abs(n1), abs(n2))
    return fr.numerator*(n1//abs(n1)), fr.denominator*(n2//(abs(n2)))

print(rat(0, 9))
inp = inp.split('\n')
asteroids = []
for x, line in enumerate(inp):
    for y, point in enumerate(line):
        if point == '#':
            asteroids.append([x, y, 0])

mx = 0
mxast = ()
for a1 in asteroids:
    ratios = []
    for a2 in [astr for astr in asteroids if astr != a1]:
        ratios.append(rat(a1[0] - a2[0], a1[1] - a2[1]))
    l = len(set(ratios))
    a1[2] = l
    if l > mx:
        mx = l
        mxast = a1

print(asteroids)
print(mxast)