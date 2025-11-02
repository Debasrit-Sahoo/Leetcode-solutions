def deleteDuplicates(head):
        dummy = ListNode(None, head)
        cur = head
        prev = dummy
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur = cur.next
                t = cur.val
                while cur and t == cur.val:
                    cur = cur.next
                prev.next = cur
            else:
                prev.next = cur
                prev = prev.next
                cur = cur.next
        return dummy.next  