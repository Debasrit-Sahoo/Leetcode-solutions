def removeNthFromEnd(head, n):
        if head == None or (head.next == None and n == 1):
            return None
        if head.next == None:
            return head
        stored = {}
        counter = 0
        cur = head
        while True:
            stored[counter] = cur
            cur = cur.next
            if cur == None:
                break
            counter += 1 
        if n > counter + 1:
            return head
        target = (counter+1) - n
        x = 0
        cur = head

        while True:
            if target == 0:
                return stored[x+1] if x+1 in stored else None
            if x == target - 1:
                cur.next = stored[x+2] if x+2 in stored else None
                return head
            cur = cur.next
            x += 1
