import copy

def check(grids, j, i, direction, depth):
    if direction == 1:
        y, x = j - 1, i
    elif direction == -1:
        y, x = j + 1, i
    elif direction == -2:
        y, x = j, i - 1
    elif direction == 2:
        y, x = j, i + 1

    oob = (y < 0) or (y >= len(grid)) or (x < 0) or (x >= len(grid))
    if oob:
        d = depth - 1
        if d < 0:
            return False
        # just the center of the grid
        c = 2
        if direction == 1:
            y, x = c - 1, c
        elif direction == -1:
            y, x = c + 1, c
        elif direction == -2:
            y, x = c, c - 1
        elif direction == 2:
            y, x = c, c + 1

        if grids[d][y][x] == '#':
            return 1
        else:
            return 0
    elif grids[depth][y][x] == '?':
        d = depth + 1
        if d >= len(grids):
            return 0

        # god help me
        if direction == 1:
            row = grids[d][-1]
            return sum([1 for t in row if t == '#'])
        elif direction == -1:
            row = grids[d][0]
            return sum([1 for t in row if t == '#'])
        elif direction == -2:
            column = [row[-1] for row in grids[d]]
            return sum([1 for t in column if t == '#'])
        elif direction == 2:
            column = [row[0] for row in grids[d]]
            return sum([1 for t in column if t == '#'])
    else:
        if grids[depth][y][x] == '#':
            return 1
        else:
            return 0

inp = """#####
.....
..?.#
#####
.###."""

grid = []
for row in inp.split('\n'):
    grid.append([tile for tile in row])
empty = [['.' for j in range(5)] for i in range(5)]
empty[2][2] = '?'
grids = [copy.deepcopy(empty) for i in range(100)] + [copy.deepcopy(grid)] + [copy.deepcopy(empty) for i in range(100)]

for i in range(200):
    ngrids = copy.deepcopy(grids)
    for d in range(len(grids)):
        for y, row in enumerate(grids[d]):
            for x, tile in enumerate(row):
                up = check(grids, y, x, 1, d)
                down = check(grids, y, x, -1, d)
                left = check(grids, y, x, -2, d)
                right = check(grids, y, x, 2, d)
                num = up+down+left+right

                if (tile == '.') and (num in [1, 2]):
                    ngrids[d][y][x] = '#'

                if (tile == '#') and (num != 1):
                    ngrids[d][y][x] = '.'
    grids = ngrids

bugs = 0
for grid in grids:
    for row in grid:
        for tile in row:
            if tile == '#':
                bugs += 1
print(bugs)