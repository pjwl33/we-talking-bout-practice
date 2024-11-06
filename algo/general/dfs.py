###################################################
# USED FOR - FIND STRONG RELATIONSHIPS IN GRAPH, FINDING ONE PATH,
# TEST IF GRAPH IS BIPARTITE, DETECTING CYCLES IN GRAPH, TOPOLOGICAL SORTING
# SOLVING PUZZLES WITH ONE SOLUTION, NETWORK ANALYSIS, MAPPING ROUTES,
# SCHEDULING A PROBLEM
# O (V + E) TC, O (V) SC
visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node) # do something with node
        visited.add(node)
        for n in graph[node]:
            dfs(visited, graph, n)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')
