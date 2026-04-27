const fs = require("fs");

function randomKey(graph) {
  const keys = Object.keys(graph);
  let vertex = keys[Math.floor(Math.random() * keys.length)];
  let neighbour =
    graph[vertex][Math.floor(Math.random() * graph[vertex].length)];
  return [vertex, neighbour];
}

function kargerMinCutAlgorithm() {
  const lines = fs.readFileSync("kargerMinCut.txt", "utf8").split("\n");
  const G = {};
  for (const line of lines) {
    const lst = line.trim().split(/\s+/);
    if (lst.length && lst[0]) G[lst[0]] = lst.slice(1); 
  }

  let u;
  while (Object.keys(G).length > 2) {
    let [u2, v] = randomKey(G);
    u = u2;
    G[u].push(...G[v]);
    for (const w of G[v]) {
      G[w] = G[w].filter((x) => x !== v);
      G[w].push(u);
    }
    G[u] = G[u].filter((x) => x !== u); 
    delete G[v];
  }

  return G[u].length;
}

function operation(n) {
  let mincut = Infinity;
  for (let i = 0; i < n; i++) {
    mincut = Math.min(mincut, kargerMinCutAlgorithm());
  }
  return mincut;
}

console.log(operation(200));

