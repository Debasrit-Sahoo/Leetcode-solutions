from typing import Optional, List
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        f = []
        s = [root]
        while s:
            r = s.pop()
            while r:
                f.append(r.val)
                if r.right: s.append(r.right)
                r = r.left
        return f