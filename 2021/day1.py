l = [int(m) for m in open('./input.txt').readlines()]
print(sum([bool(m > l[i]) for i, m in enumerate(l[1:])]))
print(sum([bool(m > l[i]) for i, m in enumerate(l[3:])]))