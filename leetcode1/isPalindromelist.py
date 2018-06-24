# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def printListNode(head):
    while head:
        print(head.val)
        head = head.next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        rev = None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            rev, slow.next, slow = slow, rev, slow.next
        # CHECK odd
        if fast:
            slow = slow.next
        while slow:
            if slow.val != rev.val:
                return False
            slow, rev = slow.next, rev.next
        return True

    #     if not head:
    #         return True
    #
    #     origin = ''
    #     cur = head
    #     while cur:
    #         origin += str(cur.val)
    #         cur = cur.next
    #     rev = self.reverseList(head)
    #
    #     reversed = ''
    #     cur = rev
    #     while cur:
    #         reversed += str(cur.val)
    #         cur = cur.next
    #
    #     return origin == reversed
    #
    # def reverseList(self,head):
    #     pre_node = None
    #     cur_node = head
    #     while cur_node:
    #         next_node = cur_node.next
    #         cur_node.next = pre_node
    #         pre_node = cur_node
    #         cur_node = next_node
    #     new_head = pre_node
    #     return new_head

def main():
    sol = Solution()
    # s = 'abobe'
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(1)
    res = sol.isPalindrome(head)
    print(res)

if __name__ == '__main__':
    main()
