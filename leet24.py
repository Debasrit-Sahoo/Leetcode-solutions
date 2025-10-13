def swapPairs(head):
    dummy = head
    cur = dummy
    p = 1
    while cur.next != None and cur.next.next != None:
        print(head)
        n1 = cur.next
        n2 = cur.next.next
        n3 = cur.next.next.next
        cur.next = n2
        cur = cur.next
        cur.next = n1
        cur = cur.next
        cur.next = n3
        print(cur)
    return head