import heapq

input = [[int(i) for i in l if i != '\n'] for l in open('./input.txt').readlines()]

def neighbours(i, j):
    n = []
    if i < len(input) - 1: n.append((i+1,j))
    if i > 0: n.append((i-1,j))
    if j < len(input[0]) - 1: n.append((i,j+1))
    if j > 0: n.append((i,j-1))
    
    return n

def dijkstra(grid):
    queue = [(0, (0, 0))]
    visited = set()
    while queue:
        risk, (i, j) = heapq.heappop(queue)

        if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
            return risk

        for n in neighbours(i, j):
            if not n in visited:
                heapq.heappush(queue, (risk + grid[n[0]][n[1]], n))
                visited.add(n)

print(dijkstra(input))

for i, row in enumerate(input):
    input[i] += [((d + j) % 9) + 1 for j in range(4) for d in row]

copy = input.copy()
for j in range(4):
    for i, row in enumerate(copy):
        input += [[((d + j) % 9) + 1 for d in row]]

print(dijkstra(input))