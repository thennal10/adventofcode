from scipy import optimize
input = [int(i) for i in open('./input.txt').readlines()[0].split(',')]

f1 = lambda x: sum([abs(x-i) for i in input])
f2 = lambda x: sum([(x-i)**2 + abs(x-i) for i in input])/2

sol = optimize.minimize(f1, x0=1)
sol = optimize.minimize(f2, x0=1)

print(f1(round(sol.x[0])))
print(f2(round(sol.x[0])))