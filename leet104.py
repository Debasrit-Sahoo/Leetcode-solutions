def maxDepth(root):
        m = 0
        def depth(root,d):
            nonlocal m
            if not root:
                m = m if d < m else d
                return d
            depth(root.left,d+1)
            depth(root.right, d+1)
        depth(root, m)
        return m if root else 0