def combine(n, k):
        save = []
        def balls(lst,cur):
            if len(lst)==k:
                save.append(lst[:])
                return
            for i in range(cur, n+1):
                lst.append(i)
                balls(lst, i+1)
                lst.pop()
        balls([],1)
        return save