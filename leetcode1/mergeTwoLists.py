# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next
        rl = head
        while l1 and l2:
            if l1.val < l2.val:
                rl.next = ListNode(l1.val)
                l1 = l1.next
            else:
                rl.next = ListNode(l2.val)
                l2 = l2.next
            rl = rl.next

        if l1:
            rl.next = l1
        if l2:
            rl.next = l2

        return head



def main():
    sol = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l2 = ListNode(1)
    # l2.next = ListNode(2)
    # l2.next.next = ListNode(4)
    rl = sol.mergeTwoLists(l1,l2)

    while rl:
        print(rl.val)
        rl = rl.next

if __name__ == '__main__':
    main()
