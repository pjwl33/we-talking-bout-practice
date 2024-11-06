# straightforward, O(mn) is bad idea
# simple improvment is O(m+n) but can be better
# in place - can it be O(1)

def setMatrixZeroes(matrix): # m x n
    # O(1)
    rows, cols = len(matrix), len(matrix[0])
    rowZero = False # check if row has a 0 or not

    # Determine which rows/cols need to be zero
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0 # set first row and col as 0
                if r > 0:
                    # only if row is greater than 0 because of top left position overlap
                    matrix[r][0] = 0
                else:
                    rowZero = True

    # need to skip the first row and col
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][r] == 0 or matrix[r][0] == 0:
                matrix[r][c] == 0

    # if origin is 0, shows us which cols can be 0
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0
    
    if rowZero:
        for c in range(cols):
            matrix[0][c] = 0