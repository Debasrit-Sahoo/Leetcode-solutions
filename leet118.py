def generate(numRows):
        out = [[1]]
        for i in range(1,numRows):
            prev = 0
            new = []
            for x in out[-1]:
                new.append(x+prev)
                prev = x
            new.append(1)
            out.append(new)
        return out