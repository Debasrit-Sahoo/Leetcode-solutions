def maxArea(List):
        i, j = 0, len(List) -1
        t = 0
        while i < j:
            t = max(min(List[i],List[j])*(j-i),t)
            if List[i] < List[j]:
                cur = List[i]
                while i < j and List[i] <= cur: 
                    i += 1
            else:
                cur = List[j]
                while i < j and List[j] <= cur:
                    j -= 1
        return t