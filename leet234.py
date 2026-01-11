class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        slow = fast = head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while stack:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True