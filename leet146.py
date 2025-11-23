class LRUCache:
    class dual_linked_list:
        def __init__(self, val = None, key = None, prev = None, next = None):
            self.val = val
            self.key = key
            self.prev = prev
            self.next = next
            self.count = 0
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = self.__class__.dual_linked_list(val = "SENT_HEAD")
        self.tail = self.__class__.dual_linked_list(val = "SENT_TAIL")
        self.head.next, self.tail.prev = self.tail, self.head

    def push_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        if len(self.map) > self.cap:
            t = self.tail.prev
            self.del_and_stitch(t)
            del self.map[t.key]
            
    def del_and_stitch(self, node, update = False):
        if node.next: node.next.prev = node.prev
        node.prev.next = node.next
        if update:
            self.push_to_head(node)

    def get(self, key):
        if key not in self.map:
            return -1
        n = self.map[key]
        self.del_and_stitch(n, True)
        return n.val
    
    def put(self, key, value):
        if key in self.map:
            d = self.map[key]
            d.val = value
            self.del_and_stitch(d, True)
        else:
            c = self.dual_linked_list(value, key)
            self.map[key] = c
            self.push_to_head(c)