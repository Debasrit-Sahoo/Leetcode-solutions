def copyRandomList(head):
        seen = {}
        def build(node):
            if not node:return None
            new = Node(node.val, build(node.next))
            seen[node] = new
            return new
        nh = cur = build(head)
        while cur and head:
            cur.random = seen.get(head.random)
            cur = cur.next
            head = head.next
        return nh.next