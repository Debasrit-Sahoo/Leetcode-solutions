def buildTree(inorder, postorder):
        index = {v: i for i, v in enumerate(inorder)}
        def build(pl, ph, il, ih):
            if il > ih:
                return None
            head = postorder[ph]
            t = index[head]
            ret = TreeNode(head)
            ret.left = build(pl, pl+ (t - il) - 1, il, t-1)
            ret.right = build(pl+ (t - il), ph - 1, t+1, ih)
            return ret
        return build(0, len(inorder)-1, 0, len(postorder)-1)