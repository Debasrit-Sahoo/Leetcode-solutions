def reverseKGroup(head, k):
        def call(cur, rest):
            end = rest
            start = cur
            while start != rest:
                nxt = start.next
                start.next = end
                end = start
                start = nxt
            return end, cur
        dummy = ListNode(0,head)
        t = dummy
        cur = head
        c = 1

        while cur.next != None:
            if c == k:
                s, tail= call(t.next, cur.next)
                t.next = s
                t = tail
                cur = t.next
                c = 1
                continue
            cur = cur.next
            c += 1
        return dummy.next