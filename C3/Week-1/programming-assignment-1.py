# Q1 & Q2 
with open('jobs.txt') as f:
    jobs = [list(map(int, line.split())) for line in f.readlines()[1:] if line.strip()]

    for job in jobs:
        job += [job[0] - job[1], job[0] / job[1]] # diff and ratio

diff = sorted(jobs, key=lambda x: (x[2], x[0]), reverse=True)
ratio = sorted(jobs, key=lambda x: (x[3], x[0]), reverse=True)

def sum_weighted_completion_time(schedule):
    ct=0
    total=0
    for job in schedule:
        ct += job[1]
        total += job[0] * ct
    return total

print(sum_weighted_completion_time(diff))
print(sum_weighted_completion_time(ratio))

# Q3
import heapq

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = []
        self.dts = float('inf')

    def add_neighbor(self, v, weight):
        if v not in [r[0] for r in self.neighbors]:
            self.neighbors.append((v, weight))

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        self.vertices[name] = Vertex(name)

    def add_edge(self, u, v, weight=0):
        self.vertices[u].add_neighbor(v, weight)
        self.vertices[v].add_neighbor(u, weight)

    def prims_mst(self, s):
        visited = set([s])
        edges = [(cost, w) for w, cost in self.vertices[s].neighbors]
        heapq.heapify(edges)
        total = 0

        while len(visited) < len(self.vertices):
            cost, v = heapq.heappop(edges)
            if v in visited:
                continue
            visited.add(v)
            total += cost
            for w, cost in self.vertices[v].neighbors:
                heapq.heappush(edges, (cost, w))

        print(total)

# Load file
g = Graph()
with open('edges.txt') as f:
    lines = f.readlines()

n = int(lines[0].split()[0])
for i in range(1, n + 1):
    g.add_vertex(i)

for line in lines[1:]:
    u, v, cost = map(int, line.split())
    g.add_edge(u, v, cost)

g.prims_mst(1)
