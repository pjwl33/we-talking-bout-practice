
def numTrees(n: int) -> int:
    # T: O(n^2), each one considered as root node, up to n
    # S: O(n), each num as root

    # numTrees[4] = numTrees[0] * numTrees[3] +
    #               numTrees[1] * numTrees[2] +
    #               numTrees[2] * numTrees[1] +
    #               numTrees[3] * numTrees[0]
    numTree = [1] * (n + 1)
    # 0 nodes = 1 tree
    # 1 nodes = 1 tree
    for nodes in range(2, n + 1):
        totalSum = 0
        for root in range(1, nodes + 1):
            left = root - 1
            right = nodes - root
            totalSum += numTree[left] * numTree[right]
        numTree[nodes] = totalSum

    return numTree[n]