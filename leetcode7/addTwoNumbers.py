# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        stack1 = []
        stack2 = []
        node = l1
        while node:
            stack1.append(node.val)
            node = node.next
        node = l2
        while node:
            stack2.append(node.val)
            node = node.next
        # print(stack1,stack2)
        overfitting = 0
        result = []
        while stack1 and stack2:
            result.append((stack1[-1]+stack2[-1]+overfitting)%10)
            overfitting = (stack1[-1]+stack2[-1]+overfitting)//10
            stack1.pop()
            stack2.pop()
        # print(result)
        while stack1:
            result.append((stack1[-1]+overfitting)%10)
            overfitting = (stack1[-1]+overfitting)//10
            stack1.pop()
        while stack2:
            result.append((stack2[-1]+overfitting)%10)
            overfitting = (stack2[-1]+overfitting)//10
            stack2.pop()
        # print(result)
        if overfitting:
            result.append(overfitting)
        head = ListNode(result.pop())
        node = head
        while result:
            node.next = ListNode(result.pop())
            node = node.next
        return head

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = 0
        while l1:
            val1 = val1 * 10 + l1.val
            l1 = l1.next

        val2 = 0
        while l2:
            val2 = val2 * 10 + l2.val
            l2 = l2.next
        total = val1 + val2
        last = None
        if total == 0:
            return ListNode(0)
        while total > 0:
            l = ListNode(total % 10)
            l.next = last
            last = l
            total /= 10
        return last
        
