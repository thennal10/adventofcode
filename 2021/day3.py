from collections import Counter
input = [l for l in open('./input.txt').readlines() if l]

count_l = [Counter([l[i] for l in input]).most_common() for i in range(len(input[0])-1)]

gamma = int(''.join([l[0][0] for l in count_l]), 2)
epsilon = int(''.join([l[1][0] for l in count_l]), 2)
print(gamma*epsilon)

def count(inp, i, o):
    c = Counter([l[i] for l in inp]).most_common()
    if len(c) == 2:
        if c[0][1] == c[1][1]:
            return '1' if o else '0'
        else:
            return c[0][0] if o else c[1][0]
    else:
        return c[0][0]

def diagnose(o):
    n_inp = input.copy()
    for i, c in enumerate(count_l):
        n_inp = list(filter(lambda x: x[i] == count(n_inp, i, o), n_inp))
        if len(n_inp) == 1:
            break
    return n_inp[0]


o2 = int(diagnose(True), 2)
co2 = int(diagnose(False), 2)
print(co2*o2)

