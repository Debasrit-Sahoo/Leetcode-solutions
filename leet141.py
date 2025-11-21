def hasCycle(head):
    f = s = head
    while f and f.next:
        s = s.next
        f = f.next.next
        if s == f:
            return True
    return False