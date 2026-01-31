class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        output = []
        l = len(num)
        def backtrack(idx, path, lastnum, sum):
            if idx == l:
                if sum == target:
                    output.append("".join(path))
                return
            else:
                for i in range(idx+1, l+1):
                    cat = num[idx:i]
                    can = int(cat)
                    path.append('+' + str(can)); backtrack(i, path, can, sum + can); path.pop()
                    path.append('-' + str(can)); backtrack(i, path, -can, sum - can); path.pop()
                    path.append('*' + str(can)); backtrack(i, path, lastnum*can, (sum-lastnum)+(can*lastnum)); path.pop()
                    if can == 0: break
        path = []
        for i in range(l):
            cat = num[0:i+1]    
            path.append(cat)
            cat = int(cat)
            backtrack(i+1, path, cat, cat)
            path.pop()
            if cat == 0: break
        return output