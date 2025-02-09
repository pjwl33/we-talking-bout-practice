class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# add the values of the nodes together in place
def mergeTrees(t1: TreeNode, t2: TreeNode):
    if not t1 and not t2:
        return None
    
    v1 = t1.val if t1 else 0
    v2 = t2.val if t2 else 0
    root = TreeNode(v1 + v2)
    root.left = mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
    root.right = mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

    return root # O(n + m), each are size of t1 and t2