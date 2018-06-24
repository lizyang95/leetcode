# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre_node = None
        cur_node = head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
        head = pre_node
        return head
    def reverseListIterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rev, cur = None, head
        while cur:
            rev, rev.next, cur = cur, rev, cur.next
        return rev
    # The recursive version is slightly trickier and the key is to work backwards.
    def reverseListRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        rev = self.reverseListRecursive(head.next)
        head.next.next = head # Reverse the tail of new reversed to list to point to current node
        head.next = None
        return rev


def printListNode(head):
    while head:
        print(head.val)
        head = head.next

def main():
    sol = Solution()
    # s = 'abobe'
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    res = sol.reverseList(head)
    print("result")
    printListNode(res)

if __name__ == '__main__':
    main()
