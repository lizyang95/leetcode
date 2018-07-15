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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or head.next == None or k == 0:
            return head

        pointer = head
        length = 1

        while pointer.next:
            pointer = pointer.next
            length += 1

        rotateTimes = k%length

        if rotateTimes == 0:
            return head

        fastPointer = head
        slowPointer = head

        for a in range (rotateTimes):
            fastPointer = fastPointer.next


        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next

        temp = slowPointer.next

        slowPointer.next = None
        fastPointer.next = head
        head = temp

        return head


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        prev = ListNode(0)
        fast = head
        slow = head
        listSize = 1

        if not head:
            return head

        while fast.next:
            fast = fast.next
            listSize += 1

        k = k % listSize

        fast.next = head
        count = listSize-k

        while count>0:
            fast = fast.next
            count -= 1

        prev.next = fast.next
        fast.next = None

        return prev.next
        


sol = Solution()
nums = [1,2,3,4,5]
nums = [1]
# nums = []
head = build_list(nums)
# printList(head)
print("result:")
printList(sol.rotateRight(head,2))
