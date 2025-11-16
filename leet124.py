def maxPathSum(root):
        m = float("-inf")
        def dfs(node):
            nonlocal m
            if not node: return 0
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            m = max(m, node.val + l + r)
            return max(l,r) + node.val
        dfs(root)
        return m