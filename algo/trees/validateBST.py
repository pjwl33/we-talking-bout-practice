class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# is it a valid BST or not
# valid meaning every left subtree from root is less than root
# every right subtree from root is greater than root

def isValidBST(root: TreeNode) -> bool:
    # DFS approach
    # O (n) = 2*n
    def valid(node, left, right): # node or left right boundaries
        if not node:
            return True # empty BST is valid
        # setting the boundaries check
        if not (node.val < right and node.val > left):
            return False
        
        return (valid(node.left, left, node.val) and
                valid(node.right, node.val, right))
    
    return valid(root, float("-inf"), float("inf"))