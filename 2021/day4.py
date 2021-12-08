input = [l for l in open('./input.txt').readlines() if l != '\n']
nums = [int(i) for i in input[0].split(',')]

def main(p1):
    lgrids = []
    grid = {}
    for i, l in enumerate(input[1:]):
        if i % 5 == 0 and i != 0:
            lgrids.append((grid, set()))
            grid = {}
        for j, n in enumerate(l.split()):
            grid[(int(n))] = (i % 5, j)
    
    lgrids.append((grid, set()))
    for num in nums:
        to_be_popped = []
        for gi, (grid, marked) in enumerate(lgrids):
            if coords:= grid.get(num):
                marked.add(coords)
            for i in range(5):
                if set([(i, j) for j in range(5)]).issubset(marked) or set([(j, i) for j in range(5)]).issubset(marked):
                    if p1:
                        unmarked = [n for n, coord in grid.items() if coord not in marked]
                        return sum(unmarked)*num
                    elif len(lgrids) == 1:
                        unmarked = [n for n, coord in grid.items() if coord not in marked]
                        return sum(unmarked)*num
                    else:
                        to_be_popped.append(gi)
                        break
        lgrids = [i for j, i in enumerate(lgrids) if j not in to_be_popped]
            

print(main(True))
print(main(False))