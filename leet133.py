def cloneGraph(node):
        if not node:
            return None
        dic = {}
        def cloner(node):
            new = Node(node.val)
            dic[node] = new
            for i in node.neighbors:
                if i.val in dic:
                    new.neighbors.append(dic[i])
                else:
                    new.neighbors.append(cloner(i))
            return new
        return cloner(node)