def Solution(l1, l2):
        head = ListNode(0)
        temp = head
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        temp.next = l1 if l1 else l2
        return head.next