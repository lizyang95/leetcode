class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:   #check if the list has two more nodes

            # partition the nodes into two parts
            pre, slow, fast = ListNode(None), head, head
            while fast and fast.next:
                pre, slow, fast = slow, slow.next, fast.next.next
            pre.next = None

            # reverse the second half
            temp = None
            while slow:
                nxt = slow.next
                slow.next = temp
                temp = slow
                slow = nxt

            # reorder two parts
            dummy = head
            while dummy and temp:
                nxt= dummy.next
                dummy.next,dummy,temp = temp, temp, nxt

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        while head is None:
            return head

        neg = -1
        pos = 1
        dummy = ListNode(0)
        dummy.next = head
        res = dummy.next

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        head = dummy.next
        for i in range(len(nums)):
            if i ==0:
                continue
            if i % 2 == 0:
                head.next = ListNode(nums[pos])
                pos +=1
                head = head.next

            else:
                head.next = ListNode(nums[neg])
                neg -= 1
                head = head.next

        head.next = None
