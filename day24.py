import copy

def check(grid, j, i, direction):
    if direction == 1:
        y, x = j - 1, i
    elif direction == -1:
        y, x = j + 1, i
    elif direction == -2:
        y, x = j, i - 1
    elif direction == 2:
        y, x = j, i + 1

    try:
        if (y >= 0) and (x >= 0) and (grid[y][x] == '#'):
            return True
        else:
            return False
    except IndexError:
        return False

inp = """#####
.....
....#
#####
.###."""

grid = []
for row in inp.split('\n'):
    grid.append([tile for tile in row])

grids = []
while True:
    ngrid = copy.deepcopy(grid)
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            up = check(grid, y, x, 1)
            down = check(grid, y, x, -1)
            left = check(grid, y, x, -2)
            right = check(grid, y, x, 2)
            num = up+down+left+right

            if (tile == '.') and (num in [1, 2]):
                ngrid[y][x] = '#'

            if (tile == '#') and (num != 1):
                ngrid[y][x] = '.'
    if ngrid in grids:
        print("HEYPOO")
        break

    grids.append(ngrid)
    grid = ngrid

bioscore = 0
for y, row in enumerate(ngrid):
    for x, tile in enumerate(row):
        if tile == '#':
            bioscore += 2**((y*len(row)) + x)
print(bioscore)