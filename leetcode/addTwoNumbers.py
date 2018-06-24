# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        exceed = 0
        if l1 == None and l2 == None:
            return None
        rl = ListNode((l1.val + l2.val + exceed)%10)
        exceed = (l1.val + l2.val + exceed)/10
        l1 = l1.next
        l2 = l2.next
        head = rl
        while l1 != None or l2 != None:
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
            rl.next = ListNode((l1.val + l2.val + exceed)%10)
            exceed = (l1.val + l2.val + exceed)/10
            l1 = l1.next
            l2 = l2.next
            rl = rl.next
        if exceed:
            rl.next = ListNode(exceed)
        return head


        # total = 0
        # tenths = 1
        # p, pp = l1, l2
        # while p or pp:
        #     if p:
        #         total += (p.val * tenths)
        #         p = p.next
        #     if pp:
        #         total += (pp.val * tenths)
        #         pp = pp.next
        #
        #     tenths *= 10
        # return [int(char) for char in str(total)[::-1]]

def main():
    sol = Solution()

    # l1 = ListNode(2)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    # l1 = ListNode(0)
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)
    #
    l1 = ListNode(5)
    l1.next = ListNode(3)
    l1.next.next = ListNode(4)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(5)

    # print(l1,l2)
    # print(sol.addTwoNumbers(l1,l2))
    rl = sol.addTwoNumbers(l1,l2)
    while rl!= None:
        print(rl.val)
        rl = rl.next


if __name__ == '__main__':
    main()
