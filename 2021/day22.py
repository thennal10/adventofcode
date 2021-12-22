import re
from collections import Counter
input = open('./input.txt').readlines()

def reboot(p1):
    cubes = Counter()

    for line in input:
        ist = line[:2]
        x1, x2, y1, y2, z1, z2 = [int(i) for i in re.findall("-?\d+", line)]
        coords = ((x1, x2), (y1, y2), (z1, z2))
        
        if p1 and not set([x1, x2, y1, y2, z1, z2]).issubset(range(-50, 51)):
            continue
        for cube, val in cubes.copy().items():
            inters_cube = []
            for ax1, ax2 in zip(coords, cube):
                inters_range = (max(ax1[0], ax2[0]), min(ax1[1], ax2[1]))
                if inters_range[1] >= inters_range[0]:
                    inters_cube.append(inters_range)
            if len(inters_cube) == 3:
                cubes[tuple(inters_cube)] -= val
        
        if ist == 'on':
            cubes[coords] += 1
    
    return sum((x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * val for ((x1, x2), (y1, y2), (z1, z2)), val in cubes.items())

print(reboot(True))
print(reboot(False))