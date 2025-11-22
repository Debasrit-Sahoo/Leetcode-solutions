def reorderList(self, head):
            if not head:
                return
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            cur = slow
            pre = None
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            cur = head
            cur = cur.next
            while pre.next:
                head.next = pre
                head = head.next
                pre = pre.next
                head.next = cur
                head = head.next
                cur = cur.next
            if pre:
                head.next = pre
                head = head.next
            head.next = None