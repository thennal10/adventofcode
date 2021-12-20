algo, grid = open('./input.txt').read().split('\n\n')

to_b = {'#': '1', '.': '0'}
grid = {(i, j): to_b[c] for i, row in enumerate(grid.split('\n')) for j, c in enumerate(row)}

gmax = max(grid, key=lambda t: t[0])[0]
rest = lambda s: '0' if (s % 2 == 0) or (algo[0] == '.') else '1'

def enhance(grid, steps):
    for k in range(steps):
        n_grid = {}
        for x in range(-k - 1, k + gmax + 2):
            for y in range(-k - 1, k + gmax + 2):
                binstr = ''
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        binstr += grid.get((x+i, y+j), rest(k))
                n_grid[(x, y)] = to_b[algo[int(binstr,2)]]
        grid = n_grid
    return sum([int(i) for i in n_grid.values()])

print(enhance(grid, 2))
print(enhance(grid, 50))