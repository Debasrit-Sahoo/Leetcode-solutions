def buildTree(preorder, inorder):
        index = {val: i for i, val in enumerate(inorder)}
        def builder(p_lo, p_hi, i_lo, i_hi):
            if i_hi <= i_lo:
                return None
            head = preorder[p_lo]
            split = index[head]
            root = TreeNode(head)
            root.left = builder(p_lo+1, p_lo+1+(split - i_lo),i_lo, split)
            root.right = builder(p_lo+1+(split - i_lo) ,p_hi , split + 1, i_hi)
            return root
        return builder(0, len(preorder), 0, len(inorder))