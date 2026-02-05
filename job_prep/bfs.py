'''
Breadth First Search

Used for trees and graphs, but graphs can have cycles, process of traversing each node of the graph.
Standard BFS traverses each vertex of the graph into 2 parts:

1) Visited
2) Not Visited

Purpose is to visit all the vertex while avoiding cycles. Starts from a node, then checks all the nodes at distance
one from the beginning node, then it checks all the nodes at distance two, and so on. So as to recollect the nodes
to be visited, BFS uses a queue (FIFO)

1. Start by putting any one of the graph's vertices at the back of the queue
2. Now take the front item of the queue and add it to the visited list
3. Create a list of that vertex's adjacent nodes. Add those which are not within the visited list to the rear of the queue.
4. Keep continuing with steps 2 and 3 until the queue is empty.

https://favtutor.com/blogs/breadth-first-search-python

Time: O(V + E)
Space: O(V)

Used for:
1. Rubik's Cube algorithm, searching for a path to convert the mess of colors to a single color
2. GPS navigation, helps in finding the shortest path availble from point A to B.
3. In pathfinding algos
4. Cycle detection in an undirected graph.
5. In minimum spanning tree.
6. To build index by search index.
7. In Ford-Fulkerson algo to find max flow in a network.
'''

graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = [] 
queue = [] # queue array collection in python

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end = " ")
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

# driver
print("Following Shortest Path for Graph using BFS")
bfs(visited, graph, '5') # starting with node 5