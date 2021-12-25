input = [l[5:].strip('\n') for l in open('./input.txt').readlines()]
a = [int(i) for i in input[5::18]]
b = [int(i) for i in input[15::18]]
div = [int(i) for i in input[4::18]]

rules = []
stack = []
for i, d in enumerate(div):
    if d == 26:
        popped = stack.pop()
        rules.append((i, popped[0], a[i] + popped[1]))
    else:
        stack.append((i, b[i]))

def main(rg):
    digit = [0]*14
    for r in rules:
        for i in rg:
            if 9 >= i + r[2] > 0:
                digit[r[1]] = i
                digit[r[0]] = i + r[2]
                break

    return "".join([str(i) for i in digit])

print(main(range(9, 0, -1)))
print(main(range(1, 10,)))