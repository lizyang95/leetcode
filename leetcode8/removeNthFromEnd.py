# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        fast=dummy
        slow = dummy
        for _ in range(n):
            fast = fast.next
        # print(fast.val)

        while fast.next:
            fast = fast.next
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next
            return dummy.next
        else:
            return None

    def printList(self,head):
        node = head
        while node:
            print(node.val)
            node = node.next
        print("")


sol = Solution()

sol= Solution()
# head = ListNode(0)
head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
sol.printList(head)
newlist = sol.removeNthFromEnd(head,1)
sol.printList(newlist)
