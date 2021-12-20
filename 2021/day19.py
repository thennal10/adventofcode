from itertools import permutations, product
import numpy as np

input = open('./input.txt').read().split('--- scanner')
input = [[np.array([int(i) for i in l.split(',')]) for l in s.split('\n')[1:] if l] for s in input[1:]]

col = set(x for i in [1, -1] for x in permutations([i, 0, 0]))
orient_matrices = np.array([[c1, c2, np.cross(c1, c2)] for c1, c2, in product(col, col) if not np.all(np.abs(c1) == np.abs(c2))])

solved = [input[0]]
unsolved = input[1:]
scanners = []

for scanner1 in solved:
    for i, scanner2 in enumerate(unsolved):
        for basis1, basis2 in product(scanner1, scanner2):
            rel1 = [sorted(np.abs(v - basis1)) for v in scanner1]
            rel2 = [sorted(np.abs(v - basis2)) for v in scanner2]
            
            intersections = [r1 for r1, r2 in product(rel1, rel2) if r1 == r2]
            if len(intersections) >= 3: 

                beacons_1 = np.transpose([scanner1[rel1.index(x)] - basis1 for x in intersections])
                beacons_2 = np.transpose([scanner2[rel2.index(x)] - basis2 for x in intersections])

                for orient in orient_matrices:
                    reoriented = orient @ beacons_2
                    if np.array_equal(beacons_1, reoriented):
                        break
                
                delta = basis1 - (orient @ basis2)
                nscanner = orient @ np.transpose(scanner2)
                nscanner = [v + (basis1 - (orient @ basis2)) for v in nscanner.transpose()]

                solved.append(nscanner)
                unsolved.pop(i)
                scanners.append(basis1 - (orient @ basis2))
                break
        
print(len(set(tuple(v) for s in solved for v in s)))
print(max([sum(np.abs(s1 - s2)) for s1, s2 in product(scanners, scanners)]))