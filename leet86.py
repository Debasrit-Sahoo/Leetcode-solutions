def partition(head,x):
        dummy = ListNode(None, head)
        dummy2 = ListNode(None,None)
        cur = head
        eh = dummy
        eh2 = dummy2
        while cur:
            if cur.val < x:
                eh.next = cur
                eh = eh.next
                cur = cur.next
            else:
                eh2.next = cur
                eh2 = eh2.next
                cur = cur.next
        eh2.next = None
        if dummy2.next:
            eh.next = dummy2.next
        return dummy.next