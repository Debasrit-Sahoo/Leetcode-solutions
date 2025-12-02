class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.inorder(root)

    def inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        o = self.stack.pop()
        v = o.val
        self.inorder(o.right)
        return v

    def hasNext(self):
        return True if self.stack else False