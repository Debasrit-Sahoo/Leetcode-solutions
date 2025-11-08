from collections import defaultdict
def levelOrder(root):
        s = defaultdict(list)
        def trav(root, d):
            if not root:
                return
            s[d].append(root.val)
            trav(root.left,d+1)
            trav(root.right,d+1)
            return
        trav(root, 0)
        out = []
        k = 0
        while k in s:
            out.append(s[k])
            k += 1
        return out