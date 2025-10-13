def generateParenthesis(n):
        valid = []
        length = 2*n
        def ffs(s, usedleft, usedright):
            if len(s) == length:
                valid.append(s)
                return
            if usedleft < n:
                ffs(s + "(", usedleft + 1, usedright)
            if usedright < usedleft:
                ffs(s + ")", usedleft, usedright + 1)

        ffs("", 0, 0)
        return valid
