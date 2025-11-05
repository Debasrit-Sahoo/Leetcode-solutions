class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        head = self
        while head:
            print(head.val)
            head = head.next
def reverseBetween(head,left,right):
        dummy = ListNode(None, head)
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
        cur = prev.next
        for _ in range(right - left):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy.next