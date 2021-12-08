from re import match
from collections import Counter
lines = [[int(x) for x in match(r'(\d+),(\d+) -> (\d+),(\d+)', l).groups()] for l in open('./input.txt').readlines()]

sign = lambda a,b: (b - a)//abs(b - a)
walker = lambda a,b: range(a, b + sign(a, b), sign(a, b))

def main(p2):
    points = Counter()
    for (x1, y1, x2, y2) in lines:
        if x1 == x2:
            for i in walker(y1, y2):
                points[(x1, i)] += 1
        elif y1 == y2:
            for i in walker(x1, x2):
                points[(i, y1)] += 1
        elif p2:
            for i, j in zip(walker(x1, x2), walker(y1, y2)):
                points[(i, j)] += 1
    return len([p for p, v in points.items() if v > 1])

print(main(False))
print(main(True))