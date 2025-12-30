class Solution:
    def h(self, n):
        x = 0
        while n:
            n = n.left
            x += 1
        return x
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        le = self.h(root.left)
        re = self.h(root.right)
        if le == re:
            return (1 << le) + self.countNodes(root.right)
        return (1 << re) + self.countNodes(root.left)
