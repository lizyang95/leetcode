# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode(0)
        large = ListNode(0)
        p1 = small
        p2 = large
        while(head):
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
            p1.next = None
            p2.next = None

        p1.next = large.next
        return small.next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newhead = None
        small = None
        bigerhead = None
        bigger = None
        cur = head
        while cur:
            nextcur = cur.next
            if cur.val < x:
                if not small:
                    newhead = small = cur
                    small.next = None
                else:
                    small.next = cur
                    small = cur
                    small.next = None
            else:
                if not bigger:
                    bigerhead = bigger = cur
                    bigger.next = None
                else:
                    bigger.next = cur
                    bigger = cur
                    bigger.next = None
            cur = nextcur
        if newhead:
            small.next = bigerhead
        else:
            newhead = bigerhead
        return newhead
