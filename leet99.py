def recoverTree(root):
        out = []
        def sleepy(n):
            if n.left:
                sleepy(n.left)
            out.append([n.val, n])
            if n.right:
                sleepy(n.right)
        sleepy(root)
        a = b = None
        for x in range(1, len(out)):
            if x > 0 and out[x-1][0] > out[x][0]:
                if not a:
                    a = out[x-1][1]
                b = out[x][1]
        a.val, b.val = b.val, a.valS