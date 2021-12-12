import networkx as nx
inp = [l.strip('\n').split('-') for l in open('./input.txt').readlines()]

G = nx.Graph(inp)

def walk(edges, node='start', count=0, visited=[], small_twice=True):
    if node == 'end':
        return 1
    elif node.islower() and node in visited:
        if not small_twice and node != 'start':
            small_twice = True
        else:
            return 0
    
    c = count
    for n2 in edges:
        c += walk(G.adj[n2], n2, count, visited + [node], small_twice)
    return c

print(walk(G.adj['start']))
print(walk(G.adj['start'], small_twice=False))