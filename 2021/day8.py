input = [[d.strip('\n').split(' ') for d in l.split(' | ')] for l in open('./input.txt').readlines()]

to_digit = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

all = {}
for k in to_digit.keys():
    try:
        all[len(k)] &= set(k)
    except KeyError:
        all[len(k)] = set(k)

p1, p2 = 0, 0
for display in input:
    segments = {c: set(o for o in 'abcdefg') for c in 'abcdefg'}
    for code in display[0]:
        for c in all[len(code)]:
            segments[c] &= set(code)
    coding = {}

    while segments:
        for c, s in segments.items():
            if len(s) == 1:
                coding[c] = s.pop()
            else:
                s -= set(coding.values())
        segments = {k:v for k,v in segments.items() if v}
    coding = {v: k for k, v in coding.items()}
    
    p1 += sum([1 for code in display[1] if len(code) in [2, 4, 3, 7]])
    p2 += (int(''.join([str(to_digit[''.join(sorted([coding[c] for c in code]))]) for code in display[1]])))

print(p1)
print(p2)