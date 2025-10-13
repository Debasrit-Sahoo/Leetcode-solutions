def generateParenthesis(n):
    ret = []
    def dsf(s , left, right):
        if left == right == n:
            ret.append(s)
            return
        if left < n:
            dsf(s + "(", left+1, right)
        if left > right:
            dsf(s + ")", left, right + 1)
    dsf("", 0 ,0)
    return ret