def detectCycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow