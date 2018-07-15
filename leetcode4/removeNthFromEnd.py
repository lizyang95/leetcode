# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head):
    node = head
    while  node:
        print(node.val)
        node = node.next


def build_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    node = head
    for num in nums[1:]:
        node.next = ListNode(num)
        node = node.next
    return head


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy.next
        length = 1
        while node.next:
            length+=1
            node = node.next
        i = 0
        node = dummy
        while i < length - n:
            node = node.next
            i+=1

        if node.next:
            node.next = node.next.next
        else:
            return None
        return dummy.next




sol = Solution()
# nums = [0,1,2,3,4,5]
nums = [1,2]
# nums = []
head = build_list(nums)
# printList(head)
print("result:")
printList(sol.removeNthFromEnd(head,2))
