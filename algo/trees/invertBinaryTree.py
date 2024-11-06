# DFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode):
    if not root:
        return None
    
    tmpNode = root.left
    root.left = root.right
    root.right = tmpNode

    invertTree(root.left)
    invertTree(root.right)
    return root