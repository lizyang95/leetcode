class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        next = dummy

        while next != None and next.next != None:
            if next.next.val == val:
                next.next = next.next.next
            else:
                next = next.next

        return dummy.next

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        out = prev = ListNode(-1)
        prev.next = head
        curr = head
        while curr:
            if curr.val==val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return out.next
