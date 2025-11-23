def insertionSortList(head):
    dummy = ListNode()
    while head:
        cur = dummy
        nex = head.next
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        head.next = cur.next
        cur.next = head
        head = nex
    return dummy.next