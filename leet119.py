def getRow(rowIndex):
        out = [[1]]
        for _ in range(1, rowIndex):
            new = []
            prev = 0
            for i in out.pop():
                new.append(i+prev)
                prev = i
            new.append(1)
            out.append(new)
        return out