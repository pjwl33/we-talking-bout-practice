class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# iterative solution
def kthSmallest(root: TreeNode, k: int) -> int:
    # n = 0
    # stack = [] # iteratively
    # curr = root

    # while curr or stack:
    #     while curr:
    #         stack.append(curr) # do before
    #         curr = curr.left
        
    #     curr = stack.pop()
    #     n += 1
    #     if n == k:
    #         return curr.val
        
    #     curr = curr.right

    # recur
    def inorder(node):
        res = []
        if node:
            res += inorder(node.left)
            res.append(node.val)
            res += inorder(node.right)
        return res
    
    return inorder(root)[k - 1]
