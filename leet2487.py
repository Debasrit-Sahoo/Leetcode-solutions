class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        m = 0
        for i in range(len(vals)-1, -1, -1):
            v = vals[i]
            if v < m: vals[i] = 0
            if m < v: m = v

        dummy = ListNode()
        cur = dummy
        for each in vals:
            if each:
                cur.next = ListNode(each)
                cur = cur.next
            
        return dummy.next