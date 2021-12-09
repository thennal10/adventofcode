from collections import Counter

input = [[int(i) for i in l if i != '\n'] for l in open('./input.txt').readlines()]

def get(x, y):
    if x in range(0, len(input)) and y in range(0, len(input[0])):
        return input[x][y]
    else:
        return 10

def sim(x, y):
    flow_dir = min((x-1,y), (x+1,y), (x,y-1), (x,y+1), key=lambda l: get(*l))
    if get(x, y) < get(*flow_dir):
        return x, y
    else:
        return sim(*flow_dir)

counter = Counter()
for i, row in enumerate(input):
    for j, num in enumerate(row):
        if num < 9:
            counter[sim(i, j)] += 1

top3 = [i[1] for i in counter.most_common()[:3]]

print(sum([get(*c) + 1 for c in counter.keys()]))
print(top3[0] * top3[1] * top3[2])