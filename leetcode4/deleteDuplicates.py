# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        dummy = ListNode(head.val-1)
        dummy.next = head
        pre = dummy
        cur = dummy.next
        while cur != None and cur.next != None:
            if pre.val == cur.val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = pre.next
                cur = pre.next

        if pre.val == cur.val:
            pre.next = cur.next

        return dummy.next

class Solution(object):
    def deleteDuplicates(self, head):
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
