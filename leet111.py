from collections import deque
def minDepth_(root):
        if not root: return 0
        arr = deque([(root,1)])
        while arr:
            root, d = arr.popleft()
            if not root.left and not root.right:
                return d
            if root.left: arr.append((root.left, d+1))
            if root.right: arr.append((root.right, d+1))