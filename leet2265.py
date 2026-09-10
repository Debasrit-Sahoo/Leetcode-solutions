class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def giv_avg_cnt(root):
            a0, a1 = giv_avg_cnt(root.left) if root.left else (0, 0)
            b0, b1 = giv_avg_cnt(root.right) if root.right else (0, 0)

            n = a1 + b1 + 1
            s = a0 + b0 + root.val

            if s//n == root.val: nonlocal ans; ans += 1

            return (s, n)

        giv_avg_cnt(root)
        return ans