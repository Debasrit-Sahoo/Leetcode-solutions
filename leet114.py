def flatten(root):
        if not root:
            return None
        l = []
        while root:
            if root.right:
                l.append(root.right)
            if root.left:
                root.right = root.left
                root.left = None
            elif l:
                root.right = l.pop()
            root = root.right
        return