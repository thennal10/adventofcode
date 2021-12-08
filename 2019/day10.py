from fractions import Fraction
from math import atan2, pi, hypot

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

inp = inp.split('\n')
asteroids = []
for y, line in enumerate(inp):
    for x, point in enumerate(line):
        if point == '#':
            asteroids.append([x, y])

mx = 0
mxast = ()
for a1 in asteroids:
    angles = []
    coords = []
    for a2 in [astr for astr in asteroids if astr != a1]:
        coords.append([a2[0] - a1[0], a1[1] - a2[1], 0])
        angles.append(atan2(a1[1] - a2[1], a2[0] - a1[0]))
    l = len(set(angles))
    if l > mx:
        mx = l
        mxast = [a1, coords]
print(mxast[0])
origin = mxast[0]
asteroids = mxast[1]
asteroids.sort(key=lambda x:(atan2(x[0], -x[1]), 1/hypot(x[0], x[1])), reverse=True)
i = 0
for c, ast in enumerate(asteroids):
    try:
        if atan2(ast[1], ast[0]) == atan2(asteroids[c+1][1], asteroids[c+1][0]):
            i += 1
            asteroids[c+1][2] = i
        else:
            i = 0
    except IndexError:
        pass

count = 0
for c in range(len(asteroids)):
    for ast in asteroids.copy():
        if ast[2] == c:
            count += 1
            if count == 200:
                print(origin[0] + ast[0], origin[1] - ast[1])
                print(ast)

            asteroids.remove(ast)

print(asteroids)