class Solution:
    def sortList(self, head):
        c = head
        a = []
        while c:
            a.append(c.val)
            c = c.next
        a.sort()
        c = head
        for x in a:
            c.val = x
            c = c.next
        return head