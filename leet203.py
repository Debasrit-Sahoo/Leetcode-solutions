class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        fake = ListNode(0, head)
        prev = fake
        p = head
        while p:
            if p.val == val:
                while p and p.val == val:
                    p = p.next
                prev.next = p
            prev = p
            p = p.next
        return fake.next