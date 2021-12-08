input = [l for l in open('./input.txt').readlines() if l]
x, y = 0, 0
for line in input:
    dir, num = line.split(' ')
    if dir == 'forward': x += int(num)
    elif dir == 'down': y += int(num)
    elif dir == 'up': y -= int(num)

print(x*y)

x, y, a = 0, 0, 0
for line in input:
    dir, num = line.split(' ')
    if dir == 'forward': 
        x += int(num)
        y += a*int(num)
    elif dir == 'down': a += int(num)
    elif dir == 'up': a -= int(num)

print(x*y) 
    