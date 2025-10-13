def swapPairs(head):
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next != None and cur.next.next != None:
            s1 = cur.next
            cur.next = cur.next.next
            cur = cur.next
            s2 = cur.next
            cur.next = s1
            cur = cur.next
            cur.next = s2
        return dummy.nextg