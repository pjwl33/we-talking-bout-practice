class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# diameter brute force - from root, go far right and far left we can
def diameter(root: TreeNode) -> int:
    res = 0

    def dfs(node):
        if not root:
            return -1 # null tree is -1, given the equation

        # H = 1 + max(L, R)
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, 2 + left + right)

        return 1 + max(left, right)
    # recursive dfs, modifying the heigh O(n) time
    dfs(root)
    return res