from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def serialize(root):

    if not root:
        return ""

    res = []
    q = deque()

    while q:
        node = q.popleft()

        if node:
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else:
            res.append("null")

    # remove trailing "null" values to match the desired format
    while res and res[-1] == "null":
        res.pop()

    return ",".join(res)


# Creating a sample tree:
#     1
#    / \
#   2   3
#      / \
#     4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

serialized = serialize(root)
print(serialized)  # Output: "null,2,null,1,null,4,3,null,5,null"

def deserialize(data):
    if not data:
        return None

    vals = data.split(",")
    root = TreeNode(int(vals[0]))
    q = [root]
    index = 1

    while q and index < len(vals):
        node = q.pop()
        # process left child
        if vals[index] != "null":
            node.left = TreeNode(int(vals[index]))
            q.append(node.left)
        index += 1
        # process right child
        if index < len(vals) and vals[index] != "null":
            node.right = TreeNode(int(vals[index]))
            q.append(node.right)
        index += 1

    return root