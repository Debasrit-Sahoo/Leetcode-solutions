class Codec:
    def serialize(self, root):
        out = []
        q = deque([root])
        while q:
            n = q.popleft()
            if n == None: out.append('#'); continue
            out.append(str(n.val))
            q.append(n.left); q.append(n.right)
        while out and out[-1] == '#': out.pop()
        return ",".join(out)
    def deserialize(self, data):
        if not data: return None
        data = data.split(',')
        if data[0] == '#': return None 
        p = 1; l = len(data)
        head = TreeNode(int(data[0]))
        q = deque([head])
        while q and p < l:
            n = q.popleft()
            if data[p] != '#':
                n.left = TreeNode(int(data[p])); q.append(n.left)
            p += 1
            if p < l and data[p] != '#':
                n.right = TreeNode(int(data[p])); q.append(n.right)
            p += 1
        return head