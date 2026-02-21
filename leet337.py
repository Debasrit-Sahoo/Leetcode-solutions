class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(n):
            if not n: return [0,0]
            l = dfs(n.left); r = dfs(n.right)
            return [max(l)+max(r), n.val+l[0]+r[0]]
        return max(dfs(root))