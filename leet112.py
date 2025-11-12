def hasPathSum(root, targetSum):
        def counter(root, s):
            s += root.val
            if not root.left and not root.right:
                return True if s == targetSum else False
            if not root.left:
                l = counter(root.left,s)
            if not root.right:
                r = counter(root.right,s)
            return (l or r)
        if not root:
            return False
        return counter(root, root.val)