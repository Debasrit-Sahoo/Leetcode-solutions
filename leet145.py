class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        final = []
        while stack:
            r = stack.pop()
            while r:
                if r.left: stack.append(r.left)
                final.append(r.val)
                r = r.right
        return final[::-1]        