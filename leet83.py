def deleteDuplicates(head):
        dummy = ListNode(None,head)
        p = dummy
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur = cur.next
            else:
                p.next = cur
                p = p.next
                cur = cur.next
        return dummy.next
            