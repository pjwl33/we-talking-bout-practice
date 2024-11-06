def wordSearch(board, word):
    # rcusrively backtracking with directions horitzontally and vertically
    # DFS
    # brute force
    rows, cols = len(board), len(board[0])
    visited = set()

    def dfs(r, c, i): # row, col, and character
        if i == len(word): # found the word at end
            return True
        
        if (r < 0 or c < 0 or
            r >= rows or c >= cols or
            word[i] != board[r][c] or
            (r, c) in visited):
            return False

        visited.add((r, c))
        res = (dfs(r + 1, c, i + 1) or 
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1))
        visited.remove((r, c))
        return res

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0): return True

    return False # O(n * m * 4^len(word))
