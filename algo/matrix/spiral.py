# Question 1: 2D Spiral Array
# Find the pattern and complete the function:
# int[][] spiral(int n);
# where n is the size of the 2D array.
# Sample Result
# input = 3
# 123
# 894
# 765
#
# input = 4
# 01 02 03 04
# 12 13 14 05
# 11 16 15 06
# 10 09 08 07
#
# input = 8
# 1 2 3 4 5 6 7 8
# 28 29 30 31 32 33 34 9
# 27 48 49 50 51 52 35 10
# 26 47 60 61 62 53 36 11
# 25 46 59 64 63 54 37 12
# 24 45 58 57 56 55 38 13
# 23 44 43 42 41 40 39 14
# 22 21 20 19 18 17 16 15
# Solution
# There are two general ways most people try to solve this problem. The most common is to find a pattern of how often you move each four directions. For example, on the 4x4 case it is 4,3,3,2,2,1. This kind of code usually has four for loops, each going one of the four directions. These kinds of solutions can very easily have bugs if you don't get the pattern exactly right or if you go too far. For example, the 1x1 case.
#
# Another way to solve this problem is to greedily traverse in each direction until you must stop, then turn around and head in the other direction. The sample code below follows this approach and is generally the best way to solve this problem.
# Sample Solution in Java
# import java.util.Arrays;
#
# public class Spiral {
#   public static int[][] genSpiral(int n) {
#    if (n<=0) {
#     throw new IllegalArgumentException("N must be >0");
#    }
#    int[] dc = new int[]{1,0,-1,0};
#    int[] dr = new int[]{0,1,0,-1};
#    int dir = 0, val=0, r=0, c=0,limit=n*n;
#    int[][] matrix = new int[n][n];
#    while (val++ < limit) {
#     matrix[r][c] = val;
#     r += dr[dir];
#     c += dc[dir];
#     if (isInvalid(matrix,r, c)) {
#      r-= dr[dir];
#      c-=dc[dir];
#      dir = (dir+1)%4;
#      r+= dr[dir];
#      c+= dc[dir];
#     }
#    }
#    return matrix;
#   }
#   private static boolean isInvalid(int[][] m, int r, int c) {
#    return r<0||c<0||r>=m.length||c>= m.length||m[r][c] != 0;
#   }
# }
# Note, however, you can also solve this problem using recursion - walk around the border and fill out the numbers with each iteration. Then, reduce the problem to a smaller square (reduced n by 2). Continue until you arrive at the base case of 1 or 0.

def spiralIterative(n):
    if n <= 0:
        raise ValueError("n must be greater than 0")

    # Init matrix the n x n with zeros
    matrix = [[0] * n for _ in range(n)]

    # Direction vectors (right, down, left, up)
    dr = [0, 1, 0, -1] # rows
    dc = [1, 0, -1, 0] # cols

    r = c = dir = 0 # start from top-left corner
    val = 1 # start fill from 1

    while val <= n * n:
        matrix[r][c] = val
        val += 1

        # Calculate next cell
        nr = r + dr[dir]
        nc = c + dc[dir]

        # Check next cell valid
        if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 0:
            r, c = nr, nc
        else:
        # Change the direction
            dir = (dir + 1) % 4
            r += dr[dir]
            c += dc[dir]

    return matrix

# Example usage
print("spiralIterative")
for row in spiralIterative(4):
    print(row)
for row in spiralIterative(8):
    print(row)


def spiralRecursive(n):
    if n <= 0:
        raise ValueError("n must be greater than 0")

    # Init matrix the n x n with zeros
    matrix = [[0] * n for _ in range(n)]

    def fillLayer(layer, val):
        if layer >= (n + 1) // 2:
            return

        # Top Row
        for i in range(layer, n - layer):
            matrix[layer][i] = val
            val += 1

        # Right Col
        for i in range(layer + 1, n - layer):
            matrix[i][n - layer - 1] = val
            val += 1

        # Bottom Row
        for i in range(n - layer - 2, layer - 1, -1):
            matrix[n - layer - 1][i] = val
            val += 1

        # Left Col
        for i in range(n - layer - 2, layer, -1):
            matrix[i][layer] = val
            val += 1

        # recursively call for next layer
        fillLayer(layer + 1, val)

    # start filling from outermost layer
    fillLayer(0, 1)

    return matrix

# Example usage
print("spiralRecursive")
for row in spiralRecursive(4):
    print(row)
for row in spiralRecursive(8):
    print(row)
