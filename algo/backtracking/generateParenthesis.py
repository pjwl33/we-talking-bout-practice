def generateParenthesis(n):
    # only add open paranethesis if open < n
    # only add a closing paranethsis if closed < open
    # valid IIF open == closed == n

    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return
        
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res