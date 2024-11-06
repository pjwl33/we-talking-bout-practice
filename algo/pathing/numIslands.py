from collections import deque

def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    visited = set()

    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))
        
        while q:
            row, col = q.popleft()
            # iterative DFS make it q.pop() - pop right
            # most recent element, than the first one
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if (nr in range(rows) and
                    nc in range(cols) and
                    grid[nr][nc] == "1" and
                    (nr, nc) not in visited
                    ):
                    visited.add((nr, nc))
                    q.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1
    
    return islands