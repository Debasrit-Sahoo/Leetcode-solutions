def isSymmetric(root):
        def mirror(left,right):
            if not left or not right:
                return True if not left and not right else False
            if left.val != right.val:
                return False
            else:
                return mirror(left.left, right.right) and mirror(left.right, right.left)
        if not root:
            return True
        return mirror(root.left, root.right)