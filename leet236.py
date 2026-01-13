class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        anc = None
        def dfs(root, l):
            nonlocal anc
            if not root:
                return
            l.append(root)
            if root == p or root == q:
                if anc:
                    for i in range(len(l)-1, -1, -1):
                        if l[i] in anc: return l[i]
                anc = set(l)
            res = dfs(root.left, l)
            if res: return res
            res = dfs(root.right, l)
            l.pop()
            return res
        return dfs(root, [])