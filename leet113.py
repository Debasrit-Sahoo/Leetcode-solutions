def pathSum(root, targetSum):
        res = []
        def trace(root,s,lst):
            s += root.val
            lst.append(root.val)
            if not root.left and not root.right:
                if s == targetSum:
                    res.append(lst[:])
                lst.pop()
                return
            l = r = False
            if root.left:
                l = trace(root.left,s,lst)
            if root.right:
                r = trace(root.right,s,lst)
            lst.pop()
            return
        if root:
            trace(root,0, [])
        return res