import math
def sumNumbers(root):
        def mf(node, val):
            if not node:
                return 0
            val = val*10 + node.val
            if not node.left and not node.right:
                return val
            return mf(node.left, val) + mf(node.right, val)
        return mf(root, 0)