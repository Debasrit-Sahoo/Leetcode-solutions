def connect(root):
        def rec(root):
            if not root or not root.left:
                return
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            rec(root.left)
            rec(root.right)
        rec(root)
        return root
