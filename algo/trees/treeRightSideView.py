from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def rightSideView(root: TreeNode) -> TreeNode:
    # BFS since we are checking the side by side of each other side
    # Level-order traversal in a tree
    # For each level, we want the right-most node
    res = []
    q = deque([root])
    
    while q:
        rightSide = None
        qLen = len(q) # this is the level at a time

        for i in range(qLen):
            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)

        if rightSide:
            res.append(rightSide.val)
    
    # all tree levels done
    return res

        