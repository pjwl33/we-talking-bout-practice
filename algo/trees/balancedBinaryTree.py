class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balancedBinaryTree(root=TreeNode) -> bool:

    # we want a pair of values, bool and height of tree
    def dfs(root):
        # base case
        if not root: return [True, 0]
        # left and right trees balanced?
        left, right = dfs(root.left), dfs(root.right)
        # from root is it balanced? AND left and right already balanced
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        # get the height at root (1) and then max of left or right
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]