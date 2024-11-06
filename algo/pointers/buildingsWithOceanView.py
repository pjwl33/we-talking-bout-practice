# Q1: Find buildings with Ocean view

# Given an array of integers that represent the height of buildings, return the indexes of the buildings that have ocean view.
# The ocean is located to the right of the buildings.

# Example:

# Input: [4, 3, 2, 3, 1]
# Output: [0, 3, 4]

#     ____
#   4 |  |  ____        ____
#   3 |  |  |  |  ____  |  |
#   2 |  |  |  |  |  |  |  |  ____
#   1 |  |  |  |  |  |  |  |  |  |
#                                   ~~~~~ Ocean
#      b0,   b1,   b2,   b3,   b4

# def oceanView(heights):
#     # [4, 3, 2, 3, 1]
#     if len(heights) <= 1:
#         return heights
    
#     res = [len(heights) - 1] # [4]
#     tallest = len(heights) - 1 # 3 
#     for i in range(heights - 2, -1): # 3
#             # 3 > 1
#         if heights[i] > heights[tallest]:
#             tallest = i
#             res.prepend(i)
#         # 
#         # l = r # 1

#     return res

def oceanView(heights):
    if not heights:
        return []

    res = []
    maxHeight = 0

    # Iterate right to left
    for i in range(len(heights) - 1, -1, -1):
        # If curr building is taller than tallest seen so far, it has ocean view
        if heights[i] > maxHeight:
            res.append(i)
            maxHeight = heights[i]

    # Since we collected buildings from right to left, reverse the result
    return res[::-1]
