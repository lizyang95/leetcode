# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        # """
        # if head == None or head.next == None:
        #     return head
        # dummy = ListNode(-1)
        # dummy.next = head
        # prepre = dummy
        # pre = head
        # cur = pre.next
        # while 1:
        #     prepre.next = cur
        #     pre.next = cur.next
        #     cur.next = pre
        #     prepre = pre
        #     if prepre.next == None or prepre.next.next == None:
        #         break
        #     pre,cur = prepre.next,prepre.next.next
        # return dummy.next

    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
