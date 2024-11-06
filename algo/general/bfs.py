###################################################
# USED FOR - PATHFINDING, GPS NAVIGATION, CYCLE DETECTION IN GRAPH
# MIN SPANNING TREE, BUILD INDEX BY SEARCH INDEX, MAX FLOW IN NETWORK
# O (V + E) TC, O (V) SC
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited, q = [], []
def bfs(visited, graph, node):
    visited.append(node)
    q.append(node)

    while q:
        m = q.pop(0)
        print(m) # do something with node
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                q.append(n)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling
