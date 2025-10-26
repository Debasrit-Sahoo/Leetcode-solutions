def rotateRight(head, k):
        if k == 0 or not head or not head.next:
            return head
        cur = head
        c = 1
        while cur.next:
            cur = cur.next
            c += 1
        if k > c:
            k = k%c
        for _ in range(k):
            cur = head
            while cur.next and cur.next.next:
                cur = cur.next
            temp = head
            head = cur.next
            head.next = temp
            cur.next = None
        return head