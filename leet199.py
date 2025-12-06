from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque([root])
        out = []
        last = None

        while stack:

            lev_len = len(stack)
            for _ in range(lev_len):

                node = stack.popleft()
                if not node: continue
                last = node.val
                stack.append(node.left)
                stack.append(node.right)

            out.append(last)
        if out: out.pop()
        return out