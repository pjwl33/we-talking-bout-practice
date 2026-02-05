# You are given a puzzel consisting of a row of squares that contain nonnegative integers, with
# a zero in the rightmost square. Keep in mind that it's possible for other squares to contain
# a zero. You have a token that starts on the leftmost square.

# On each turn, the token can shift left or right a number of sqaures exactly equal to the value 
# in its current square, but is not allowed to move off either end. For example if the row of 
# squares contains these values: [2, 0, 5, 3, 1, 3, 1, 4, 0], then on the first turn the only legal
# move is to shift right two squares, because the starting square contains a 2, and the token
# can't move off the left end. 

# The goal is to get the token to the rightmost square. This row has a solution (more than one),
# but not all rows do. If we start with the row [1, 3, 2, 1, 3, 4, 0], then there is no way for 
# the token to reach the rightmost square.

# Write a recursive function named "row_puzzle" that takes a list of integers (the row) as a
# parameter and returns True if the puzzle is solvable for that row, but returns False otherwise.
# After the function has finished, the list must be the same as it was when the function was called.

# You may use default arguments and/or helper functions.

# Your recursive function must not:
# - Use any loops
# - Use any variables declared outside of the recursive function
# - Use any mutable default arguments (see the Cody Style Requirements)

# Hint 1: Your recursive function should always try both directions. You want it to explore all
# the possibilites, and again, you should avoid trying to look ahead to see if a direction 
# wouldn't work out at the next level of recursion. Let each level worry about itself.

# Hint 2: If there are possible cycles (as in the first example above), then there are an 
# infinite number of valid paths, but if there is any valid path, then there is a valid path 
# that doesn't visit any index more than once, so you only need to worry about paths that don't 
# revisit indices. You may find memoization useful for keeping track of what indices have been
# visited.

# Hint 2.a: To add the memo parameter, you cna use either a helper function or a default argument.
# If you want to add it using a default argument, make sure it is not mutable.

# Hint 2.b: Use a set for the memoization. Testing membership in a list of tuple uses iteration,
# but not in a set or dictionary. Also, testing membership in a set or dictionary is faster -
# O(1) instead of O(n)

def row_puzzle(row):

    def solvable(position, visited):
        # Base Case: If the token reaches the rightmost (last position), then it is True
        if position == len(row) - 1:
            return True
        
        # Cycle Prevention: If the position has already been visited, it's in a cycle loop 
        # and therefore cannot complete
        if position in visited:
            return False
        
        # Add the visited position to the set to keep track
        visited.add(position)

        # Check current move count from the row based on position
        move = row[position]

        # Check the right movement possibility
        if position + move < len(row) and solvable(position + move, visited):
            return True

        # Check the left movement possibility
        if position - move >= 0 and solvable(position - move, visited):
            return True
        
        # If neither direction work, then it cannot be solved
        return False
    
    # Call the recursive function starting at position 0 with a new set
    return solvable(0, set())

can_solve = [2, 0, 5, 3, 1, 3, 1, 4, 0]
cannot_solve = [1, 3, 2, 1, 3, 4, 0]
print("Checking for [2, 0, 5, 3, 1, 3, 1, 4, 0]", row_puzzle(can_solve))
print("Checking for [1, 3, 2, 1, 3, 4, 0]", row_puzzle(cannot_solve))