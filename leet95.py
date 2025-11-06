def numTrees(n): 
        def build(lo,hi):
            if lo>hi:
                return [None]
            save = []
            for root in range(lo, hi+1):
                for left in build(lo, root-1):
                    for right in build(root+1, hi):
                        save.append(TreeNode(root, left, right))
            return save
        return build(1,n)