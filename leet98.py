def isValidBST(root):
        def lua(node, lo, hi):
            if not node:
                return True
            if lo < node.val < hi:
                return lua(node.left,lo, node.val) and lua(node.right,node.val, hi)
            return False
        return lua(root, float("-inf"), float("inf"))
def mf(root):
        if not root:
            return False
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, lo, hi = stack.pop()
            if not node:
                continue
            if not (lo < node.val < hi):
                return False
            stack.append((node.left, lo, node.val))
            stack.append((node.right,node.val, hi))
        return True