# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head

        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        k = k%length
        if not k:
            return head
        fast = head
        slow = head
        pre = ListNode(-1)
        for _ in range(k-1):
            fast = fast.next
        while fast.next:
            fast = fast.next
            pre = slow
            slow = slow.next

        pre.next = None
        fast.next = head

        return slow


    def printList(self,head):
        node = head
        while node:
            print(node.val)
            node = node.next
        print("")

sol= Solution()
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
sol.printList(head)
newlist = sol.rotateRight(head,4)
