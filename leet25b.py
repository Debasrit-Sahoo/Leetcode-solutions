def reverseKGroup(head, k):
        def reverser(start, end):
            cur = start
            rest = end
            while cur != end:
                nxt = cur.next
                cur.next = rest
                rest = cur
                cur = nxt
            return rest, start #head, tail
        dummy = ListNode(0,head)
        cur = head
        hed = dummy
        n = 1
        while cur:
            if n == k:
                temp, tail = reverser(hed.next, cur.next)
                hed.next = temp
                hed = tail
                cur = tail.next
                n = 1
            else:
                n += 1
                cur = cur.next
        return dummy.next