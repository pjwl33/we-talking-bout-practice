def rotateImage(matrix): # n x n
    # need to do in place, no copy and use more memory
    # O(n * n) for matrix run time, and O(1) memory
    l, r = 0, len(matrix) - 1

    while l < r:
        # as i in incremented, we shift the rotate angle by one
        for i in range(r - 1):
            t, b = l, r
            # save the topLeft val
            topLeft = matrix[t][l + i]
            # move the bottom left to top left
            matrix[t][l + i] = matrix[b - i][l]
            # move the bottom right into bottom left
            matrix[b - i][l] = matrix[b][r - i]
            # move the top right into the bottom right
            matrix[b][r - i] = matrix[t + i][r]
            # move the top left into the top right
            matrix[t + i][r] = topLeft
        
        # update pointers
        r -= 1
        l += 1