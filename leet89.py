def grayCode1(n):
        def backtrack(n):
            if n == 1:
                return [[0], [1]]
            else:
                half = backtrack(n-1)
                other_half = []
                for x in half:
                    other_half.append(x+[1])
                    x.append(0)
                other_half.reverse()
                half.extend(other_half)
                return half
        res = backtrack(n)
        return ["".join(map(str,(i[::-1]))) for i in res]

def grayCode(n):
    return [i ^ (i >> 1) for i in range(1 << n)]