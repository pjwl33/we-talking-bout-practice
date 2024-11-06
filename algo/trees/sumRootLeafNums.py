class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# preorder traversal, process the parent node before children
def sumNumbers(root: TreeNode) -> int:

    def dfs(curr, sum): # for sum == current sum
        if not curr:
            return 0
        
        sum = sum * 10 + curr.val

        if not curr.left and not curr.right: # it's a leaf node
            return sum
        
        return dfs(curr.left, sum) + dfs(curr.right, sum)
    
    return dfs(root, 0) # O(n) traversing the entire tree, memory is height of tree