def isSameTree(p, q):
        def check(p,q):
            if not p or not q:
                return False if p != q else True
            if p.val != q.val:
                return False
            else:
                return check(p.left, q.left) and check(p.right, q.right)