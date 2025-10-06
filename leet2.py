# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
        def addTwoNumbers(self, l1, l2, carry=0):
            if not l1 and not l2 and not carry:
                return None
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            out = a + b + carry
            carry = out // 10
            out = out % 10
            return ListNode(out, self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None, carry))
            