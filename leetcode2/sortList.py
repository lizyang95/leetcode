# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head == None or head.next == None:
        #     return head
        # slow = head
        # fast = head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # head1 = head
        # head2 = slow.next
        # slow.next = None
        # head1 = self.sortList(head1)
        # head2 = self.sortList(head2)
        # head = self.merge(head1,head2)
        # return head
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))

    # def merge(self,head1,head2):
    #     if head1 == None:
    #         return head2
    #     if head2 == None:
    #         return head1
    #     dummy = ListNode(0)
    #     p = dummy
    #
    #     while head1 and head2:
    #         if head1.val < head2.val:
    #             p.next = head1
    #             head1 = head1.next
    #             p = p.next
    #         else:
    #             p.next = head2
    #             head2 = head2.next
    #             p = p.next
    #     if head1 == None:
    #         p.next = head2
    #     if head2 == None:
    #         p.next = head1
    #     return dummy.next
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next

        tail.next = h1 or h2
        return dummy.next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        slow = ListNode(0)
        slow.next = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1,head2 = head,slow.next
        slow.next = None
        tmp1,tmp2 = self.sortList(head1),self.sortList(head2)
        ans = ListNode(0)
        p = ans
        while tmp1 and tmp2:
            if tmp1.val < tmp2.val:
                p.next = tmp1
                tmp1,p = tmp1.next,p.next
            else:
                p.next = tmp2
                tmp2,p = tmp2.next,p.next
        if tmp1:
            p.next = tmp1
        if tmp2:
            p.next = tmp2
        return ans.next
