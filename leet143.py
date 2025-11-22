from collections import deque
def reorderList(head):
        stack = deque([])
        s = head
        while s:
            stack.append(s)
            s = s.next
        cur = head
        while len(stack) >= 2:
            left, right = stack.popleft(), stack.pop()
            cur.next = left
            cur = cur.next
            cur.next = right
            cur = cur.next
        if stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None