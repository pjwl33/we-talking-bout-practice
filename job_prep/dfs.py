'''
Depth First Search

1. Start by putting any one of graph's vertex on top of stack (LIFO)
2. Take top item of stack and add to visited list of vertex
3. Create list of that adjacent node of the vertex, add the ones which aren't in the visited list of vertexes to top of stack
4. Keep repeationg steps 2 and 3 until stack is empty

https://favtutor.com/blogs/depth-first-search-python

Time: O(V + E)
Space: O(V)

Used for:
1. Finding the strongly connected components of the graph
2. For finding the path (1 solution)
3. To test if the graph is bipartite (where vertices can be divided into 2 disjoint sets such that
    all the edges connect a vertext in one set to a vertex in a nother set)
4. For detecting cycles in a graph
5. Topoligcal Sorting
6. Sovling the puzzle with only one solution
7. Network Analysis
8. Mapping Routes
9. Scheduling a problem
'''

graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = set() # stack use collection in python

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for n in graph[node]:
            dfs(visited, graph, n)

# driver
print("Following Graph using DFS")
dfs(visited, graph, '5') # starting with node 5