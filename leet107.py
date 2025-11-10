from collections import defaultdict
def levelOrderBottom(root):
        if not root:
             return []
        ret = defaultdict(list)
        m = 0
        def traverser(d, node):
            nonlocal m
            if not node:
                return
            if d > m: m = d
            ret[d].append(node.val)
            traverser(d+1, node.left)
            traverser(d+1, node.right)
        traverser(0, root)
        out = []
        while m >= 0:
            out.append(ret[m])
            m -= 1
        return out