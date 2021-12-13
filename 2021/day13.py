import numpy as np

dots_data, fold_data = open('./input.txt').read().split('\n\n')
dots = {tuple(int(i) for i in l.split(',')) for l in dots_data.split()}
folds = [(f[11], int(f[13:])) for f in fold_data.split('\n')]

for f, fold in enumerate(folds):
    i = 0 if fold[0] == 'x' else 1
    below = {d for d in dots if d[i] > fold[1]}
    image = {(d[not i], 2*fold[1] - d[i])[:: 1 if i else -1] for d in below}
    dots =  (dots | image) - below
    
    if f == 0: print(len(dots))

grid = np.full((max([d[1] for d in dots]) + 1, max([d[0] for d in dots]) + 1), ' ')
for d in dots:
    grid[d[::-1]] = '#'
for line in grid:
    print(''.join(line))