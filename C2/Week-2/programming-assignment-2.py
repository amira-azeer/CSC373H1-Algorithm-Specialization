import heapq

def parse_graph(filename):
    graph = {}
    with open(filename) as f:
        for line in f:
            parts = line.split()
            u = int(parts[0])
            graph.setdefault(u, [])
            for entry in parts[1:]:
                v, w = map(int, entry.split(','))
                graph.setdefault(v, [])
                graph[u].append((v, w))
                graph[v].append((u, w))
    return graph

def dijkstra(graph, source, targets):
    dist = {n: 1000000 for n in graph}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return ','.join(str(dist[t]) for t in targets)

graph = parse_graph('dijkstraData.txt')
targets = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
print(dijkstra(graph, 1, targets))
