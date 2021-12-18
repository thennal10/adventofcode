from json import loads
import re
import math
input = [l.strip('\n') for l in open('./input.txt').readlines()]


def explode(snailnum):
    caretnum = 0
    last_d = None
    exploded = None
    next_d = None
    for i, c in enumerate(snailnum):
        if c in ['[',']']:
            caretnum += 1 if c == '[' else -1
            if caretnum == 5:
                try:
                    exploded = re.search('(\d+),(\d+)' , snailnum[i:])
                    exploded = (exploded.groups(), exploded.start() + i, exploded.end() + i)
                except Exception:
                    pass
                
                try:
                    last_d = [match for match in re.finditer('\d+', snailnum[:i])][-1]
                    last_d = (last_d.start(), last_d.end())
                except Exception:
                    pass
                
                try:
                    next_d = re.search('\d+', snailnum[exploded[2]:])
                    next_d = (next_d.start() + exploded[2], next_d.end() + exploded[2])
                except Exception:
                    pass
                break

    if not exploded:
        return None

    nsnail = ''

    if last_d:
        new_l = int(exploded[0][0]) + int(snailnum[last_d[0]:last_d[1]])
        nsnail += snailnum[:last_d[0]] + str(new_l)   
        nsnail += snailnum[last_d[1]: exploded[1]-1] + '0'
    else:
        nsnail += snailnum[: exploded[1]-1] + '0'
    if next_d:
        new_r = int(exploded[0][1]) + int(snailnum[next_d[0]:next_d[1]])
        nsnail += snailnum[exploded[2]+1:next_d[0]] + str(new_r)
        nsnail += snailnum[next_d[1]:]
    else:
        nsnail += snailnum[exploded[2]+1:]
    
    return nsnail

def split(snailnum):
    for match in re.finditer('\d+', snailnum):
        i = int(match.group())
        if i > 9:
            splitpair = f'[{math.floor(i/2)},{math.ceil(i/2)}]'
            return snailnum[:match.start()] + splitpair + snailnum[match.end():]
    else:
        return None

def action(snailnum):
    for func in [explode, split]:
        reduced = func(snailnum)
        if reduced:
            return action(reduced)
    
    return reduced if reduced else snailnum

def magnitude(snailnum):
    l, r = snailnum
    if isinstance(l, list):
        l = magnitude(l)
    if isinstance(r, list):
        r = magnitude(r)
    return (3*l) + (2*r)
    

totalsnail = input[0]
for snailnum in input[1:]:
    totalsnail = f'[{totalsnail},{snailnum}]'
    totalsnail = action(totalsnail)

maglist = set()
for snailx in input:
    for snaily in input: 
        nsnail = f'[{snailx},{snaily}]'
        reducedsnail = action(nsnail)
        maglist.add(magnitude(loads(reducedsnail)))

print(magnitude(loads(totalsnail)))
print(max(maglist))