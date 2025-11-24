class Solution:
    def split(self, head):
        if not head or not head.next:
            return head,None
        
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        h = slow.next
        slow.next = None       
        return head, h
    def merge(self, l, r):
        if l ^ r: return l if not r else r
        if l.val > r.val:
            r.next = self.merge(l, r.next)
            return r
        else:
            l.next = self.merge(l.next, r)
            return l
    def sortList(self, head):
        if not head or not head.next:
            return head
        a,b = self.split(head)
        a = self.sortList(a)
        b = self.sortList(b)
        return self.merge(a,b)