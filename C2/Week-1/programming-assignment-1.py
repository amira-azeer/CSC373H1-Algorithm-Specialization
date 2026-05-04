from collections import defaultdict

NUM_NODES = 875715  # 875715 so range(1, NUM_NODES) includes 875714

graph = defaultdict(list)           # original graph
reversed_graph = defaultdict(list)  # reversed / transpose graph
visited = set()                     # tracks visited nodes
scc_sizes = []                      # stores SCC sizes as a plain list
stack = []                          # DFS stack
order = []                          # finishing order to guide Pass 2

# Read file and build both graphs in one pass
with open('SCC.txt', 'r') as file:
    for line in file:
        u, v = map(int, line.split())  # unpack both values as integers
        graph[u].append(v)             # original edge u → v
        reversed_graph[v].append(u)    # reversed edge v → u

# Pass 1 - DFS on reversed graph to get finishing order
for node in range(1, NUM_NODES):
    if node in visited:
        continue
    visited.add(node)
    stack.append(node)

    while stack:
        curr = stack[-1]
        neighbors = reversed_graph[curr]
        if neighbors:
            neighbor = neighbors.pop()
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
        else:
            order.append(stack.pop())  # node finished, record it

# Pass 2 - DFS on original graph in reverse finishing order
visited = set()   # reset visited
order.reverse()   # process in reverse finishing order

for node in order:
    if node in visited:
        continue
    visited.add(node)
    stack.append(node)
    temp = []  # holds all nodes in this SCC

    while stack:
        curr = stack[-1]
        neighbors = graph[curr]
        if neighbors:
            neighbor = neighbors.pop()
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
        else:
            temp.append(stack.pop())  # node finished, add to SCC

    scc_sizes.append(len(temp))       # store size of this SCC

# Output top 5
scc_sizes.sort(reverse=True)         # sort list of sizes — this works unlike defaultdict
top5 = scc_sizes[:5]

while len(top5) < 5:
    top5.append(0)                    # pad with 0s if fewer than 5 SCCs

print(",".join(map(str, top5)))
