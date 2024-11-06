# Q2: Binary Tree Lowest Common Ancestor

# Given a binary tree and two nodes in that tree, find the lowest common ancestor of those nodes.

# Example:
#     3
#    / \
#   9   7
#  / \   \
# 2   6   4

# 2, 6 -> 9
# 7, 6 -> 3
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Base Case:

# If the current node is None, return None.
# If the current node is either n1 or n2, then this node itself is an ancestor (potentially the LCA if the other node is found in the other subtree).

# Recursive Case:

# Recursively search for n1 and n2 in the left and right subtrees.
# If both left and right recursive calls return a non-None result, it means one node is in the left subtree and the other is in the right subtree. Therefore, the current node is their lowest common ancestor.
# If only one of the recursive calls returns a non-None result, return that result as it is the LCA or an ancestor in that subtree.

# Return Value:

# If both nodes are found on different branches, the current node is the LCA.
# If only one node is found, continue returning up the tree with the found node.

def commonAncestor(root, n1, n2):
    # Base case if we reach the end of a branch of find either node:
    if root is None or root.value == n1 or root.value == n2:
        return root

    # Recurse on the left and right subtrees
    left = commonAncestor(root.left, n1, n2)
    right = commonAncestor(root.right, n1, n2)

    # If both left and right are non-null, we've found the LCA
    if left and right:
        return root

    # Otherwise, return the non-null result
    return left if left else right


# Construct the binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.right = TreeNode(4)

# Find common ancestors
lca1 = commonAncestor(root, 2, 6)
print(lca1.value)  # Output: 9

lca2 = commonAncestor(root, 7, 6)
print(lca2.value)  # Output: 3
