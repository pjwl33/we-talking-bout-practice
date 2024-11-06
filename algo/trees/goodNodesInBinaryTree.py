class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Preorder traversal, process each node
# input: root = [3, 1, 4, 3, null, 1, 5]
# output: 4
# Explanation: Nodes in blue are good - Root Node (3) is always a good node
# Node 4 -> (3, 4) is the max value in the path starting from the root
def goodNodes(root: TreeNode) -> int: 

    # max value from root to every node down
    def dfs(node, maxValue):
        if not node:
            return 0 # empty tree has no good nodes
        
        res = 1 if node.val >= maxValue else 0
        maxValue = max(maxValue, node.val)
        res += dfs(node.left, maxValue)
        res += dfs(node.right, maxValue)
        return res
    
    return dfs(root, root.val) # root node always counts as good node