from collections import defaultdict, deque, Counter
def minWindow(s, t):
        need = Counter(t)
        have = defaultdict(int)
        out = [0,float("inf")]
        count = 0
        i,j = 0, 0
        while j < len(s):
            while j < len(s) and s[j] not in need:
                j += 1
            if j == len(s):
                break
            have[s[j]] += 1
            if have[s[j]] == need[s[j]]:
                count += 1
            j += 1
            while count == len(need):
                if not out or out[1] - out[0] > j-i:
                    out = [i,j]
                if s[i] in need:
                    have[s[i]]-=1
                    if have[s[i]] < need[s[i]]:
                        count -= 1
                i += 1
                while i < j and s[i] not in need:
                    i += 1
        if out[1] != float("inf"):
            return s[out[0]:out[1]]
        return ""