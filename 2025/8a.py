import math
def euclideanDistance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)

parent = {}
size = {}

def make_set(v):
    parent[v] = v
    size[v] = 1

def find_set(v):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]

def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

with open('8.txt') as f:
    coords = []
    for line in f:
        x,y,z = line.strip().split(',')
        coords.append([int(x), int(y), int(z)])
    edges = []
    for i in range(len(coords)):
        make_set(i)
        for o in range(i+1, len(coords)):
            edges.append([euclideanDistance(coords[i], coords[o]), i, o])
    edges.sort()

    connected = set()
    connections = 0
    x = 0
    while connections < 1000:
        dist, i, o = edges[x]
        x += 1
        connections += 1
        union_sets(i, o)
        connected.add(i)
        connected.add(o)

    done = set()
    sizes = []
    for i in range(len(coords)):
        p = find_set(i)
        if p in done:
            continue
        done.add(p)
        sizes.append(size[p])
    sizes.sort(reverse=True)
    print(math.prod(sizes[:3]))
