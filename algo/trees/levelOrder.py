from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode):
    # BFS with a queue
    res = []
    q = deque()
    q.append(root)
    # BFS
    while q:
        qLen = len(q) # ensure 1 level at a time
        level = []
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)

    # memory O(n / 2)
    return res

