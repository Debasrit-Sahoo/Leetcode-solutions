def isBalanced(root):
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return left + 1 if left > right else right + 1
        if not root or helper(root) != -1:
            return True
        return False