def Solution(l1, l2):
        head = ListNode(0)
        curr = head
        while not (l1 == None and l2 == None):
            a = l1.val if l1 != None else float("-inf")
            b = l2.val if l2 != None else float("-inf")
            x1 = a if a>b else b
            x2 = b if a>b else a
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            if x1 == float("-inf"):
                curr.next = ListNode(x2)
                curr = curr.next
                continue
            if x2 == float("-inf"):
                curr.next = ListNode(x1)
                curr = curr.next
                continue
            else:
                curr.next = ListNode(x2)
                curr = curr.next
                curr.next = ListNode(x1)
                curr = curr.next
        return head.next
