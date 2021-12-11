import numpy as np
input = np.array([[int(i) for i in l if i != '\n'] for l in open('./input.txt').readlines()])

def get_adjacent(i, j):
    adj = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            r = range(0, 10)
            (x, y) = (i+dx, j+dy)
            if (x in r) and (y in r) and (dx, dy) != (0, 0):
                adj.append((x, y))
    return adj

p1 = 0
p2 = None
step = 0
while not p2:
    step += 1
    input = input + 1
    while (input > 9).any():
        for i, j in np.transpose((input > 9).nonzero()):
            input[i][j] = -10**3
            for x, y in get_adjacent(i, j):
                input[x][y] += 1
    
    if (input < 0).all(): 
        p2 = step
    
    if step <= 100:
        p1 += (input < 0).sum()
    
    input[input < 0] = 0


print(p1)
print(p2)