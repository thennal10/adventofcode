input = open('./input.txt').readlines()[0][13:]
tx, ty = [[int(i) for i in x[2:].split('..')] for x in input.split(', ')]

def xpos(v, n):
    if n < v: return ypos(v, n)
    else: return v*(v+1)//2

def ypos(v, n): return n*v - (n*(n-1)//2)

count = 0
for vx in range(0, tx[1] + 1):
    for vy in range(ty[0], -ty[0]):
        x, y, n = 0, 0, 0
        while x < tx[1] and y > ty[0]:
            x, y = xpos(vx, n), ypos(vy, n)
            if tx[0] <= x <= tx[1] and ty[0] <= y <= ty[1]:
                count += 1
                break
            n += 1

print(xpos(-1-ty[0],-ty[0]))
print(count)