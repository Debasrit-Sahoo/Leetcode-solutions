class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        out = []
        def dfs(r, l):
            l.append(str(r.val))
            if not (r.left or r.right): out.append("->".join(l)); l.pop(); return
            if r.left: dfs(r.left, l)
            if r.right: dfs(r.right, l)
            l.pop()
        if root: dfs(root, [])
        return out