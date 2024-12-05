f = open("5.txt")

edges = []
for line in f:
    if line[0] == "\n":
        break
    u, v = line.strip().split("|")
    edges.append([int(u), int(v)])

sum = 0
for line in f:
    pageOrder = line.strip().split(",")
    pageOrder = [int(page) for page in pageOrder]
    graph = {page: { "inDegree": 0, "edges": [] } for page in pageOrder}
    for u, v in edges:
        if u not in graph or v not in graph:
            continue
        graph[u]["edges"].append(v)
        graph[v]["inDegree"] += 1

    correctOrder = []
    q = []
    for page in pageOrder:
        if graph[page]["inDegree"] == 0:
            q.append(page)

    while q:
        u = q.pop()
        correctOrder.append(u) 
        for v in graph[u]["edges"]:
            graph[v]["inDegree"] -= 1
            if graph[v]["inDegree"] == 0:
                q.insert(0, v)
    if pageOrder != correctOrder:
        sum += correctOrder[len(correctOrder)//2]

print(sum)
