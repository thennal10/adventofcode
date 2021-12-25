from copy import deepcopy
input = [list(i.strip('\n')) for i in open('./input.txt').readlines()]

jmax, imax = len(input[0]), len(input)
step = 1
while True:
    ninput = deepcopy(input)
    for i, row in enumerate(input):
        for j, c in enumerate(row):
            if c == '>':
                if row[(j+1) % jmax] == '.':
                    ninput[i][j] = '.'
                    ninput[i][(j+1) % jmax] = '>'
    input_mod = deepcopy(ninput)
    for i, row in enumerate(input_mod):
        for j, c in enumerate(row):
            if c == 'v':
                if input_mod[(i+1) % imax][j] == '.':
                    ninput[i][j] = '.'
                    ninput[(i+1) % imax][j] = 'v'
    if input == ninput:
        print(step)
        break
    input = ninput
    step += 1