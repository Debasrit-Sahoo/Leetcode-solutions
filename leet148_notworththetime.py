class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        size = 1
        s = head
        length = 0
        while s:
            s = s.next
            length += 1
        block = 1
        while block < length:
            prev = dummy = ListNode()
            main = head
            c = 0
            while c < length:
                p1 = p2 = main
                c1 = 0
                while c1 != block and p2:
                    p2 = p2.next
                    c1 += 1
                main = p2
                c1 = 0
                while c1 != block and main:
                    c1 += 1
                    main = main.next
                c1 = c2 = 0
                while p1 and p2 and c1 < block and c2 < block:
                    if p1.val <= p2.val:
                        prev.next = p1
                        p1 = p1.next
                        c1 += 1
                    else:
                        prev.next = p2
                        p2 = p2.next
                        c2 += 1
                    prev = prev.next
                while p2 and c2 != block:
                    prev.next = p2
                    p2, prev = p2.next, prev.next
                    c2 += 1
                while p1 and c1 != block:
                    prev.next = p1
                    p1, prev = p1.next, prev.next
                    c1 += 1
                prev.next = None
                c += block*2
            head = dummy.next
            block <<= 1
        return head