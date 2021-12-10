input = [l.strip('\n') for l in open('./input.txt').readlines()]

closedict = {'{': '}', '(': ')', '[': ']', '<': '>'}
p1dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
p2dict = {')': 1, ']': 2, '}': 3, '>': 4}
opens = []
p1 = 0
p2list = []
for line in input:
    p2 = 0
    for c in line:
        if c in '{([<':
            opens.append(c)
        elif c == closedict[opens[-1]]:
            opens.pop(-1)
        else:
            p1 += p1dict[c]
            opens = []
            break
    if opens:
        closes = [closedict[c] for c in opens[::-1]]
        for c in closes:
            p2 = (p2*5) + p2dict[c]
        opens = []
        p2list.append(p2)

print(p1)
print(sorted(p2list)[(len(p2list)-1)//2])