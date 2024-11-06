class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# using 2 points - binary

def sortedArraytoBST(nums: List[int]) -> TreeNode:
    # what portion of input nums we are trying to convert into a tree
    def helper(l, r):
        if l > r:
            return None
        
        m = (l + r) // 2
        root = TreeNode(nums[m])
        root.left = helper(l, m - 1)
        root.right = helper(m + 1, r)
        return root

    return helper(0, len(nums) - 1)
    # O(n) Memory is O(logn) height of the tree