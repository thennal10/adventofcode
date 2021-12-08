from collections import Counter

input = open('./input.txt').readlines()[0]
fishlist = [int(i) for i in input.split(',')]

def grow(days):
    counter = Counter(fishlist)
    for i in range(days):
        new = counter[0]
        for j in range(8):
            counter[j] = counter[j+1]
        counter[6] += new
        counter[8] = new
    return sum(counter.values())

print(grow(80))
print(grow(256))