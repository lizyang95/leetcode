# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node.val = node.next.val
        node.next = node.next.next
