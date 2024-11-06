class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def robberThree(root: TreeNode) -> int:
    # cannot rob adj houses
    # return [withRoot, withoutRoot]
    def dfs(node):
        if not root:
            return [0, 0]
        
        leftPair = dfs(root.left)
        rightPair = dfs(root.right)
        # with the root
        withRoot = root.val + leftPair[1] + rightPair[1]
        # without the root
        withoutRoot = max(leftPair) + max(rightPair)
        return [withRoot, withoutRoot]

    return max(dfs(root)) # O(n)