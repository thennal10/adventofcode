import networkx as nx
inp = [l.strip('\n').split('-') for l in open('./input.txt').readlines()]

G = nx.Graph(inp)

def walk(node='start', count=0, visited=[], small_twice=False):
    if node == 'end':
        return 1
    elif node.islower() and node in visited:
        if not small_twice and node != 'start':
            small_twice = True
        else:
            return 0
    
    c = count
    for n2 in G.adj[node]:
        c += walk(n2, count, visited + [node], small_twice)
    return c

print(walk(small_twice=True))
print(walk())