def inorderTraversal(root):
        out = []
        def sleepy(n):
            if n.left:
                sleepy(n.left)
            out.append(n.val)
            if n.right:
                sleepy(n.right)
        sleepy(root)
        return out
