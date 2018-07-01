# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        pre = head
        cur = pre.next
        while cur != None:
            if cur.val> pre.val:
                pre = pre.next
                cur = pre.next
            else:
                tmppre = head
                tmpcur = tmppre.next
                if cur.val <= tmppre.val:
                    tmpNode = ListNode(cur.val)
                    tmpNode.next = tmppre
                    head = tmpNode
                    pre.next = cur.next
                    cur = pre.next
                    continue
                while tmpcur.val < cur.val:
                    tmppre = tmppre.next
                    tmpcur = tmppre.next
                tmpNode = ListNode(cur.val)
                tmppre.next = tmpNode
                tmpNode.next = tmpcur
                pre.next = cur.next
                cur = pre.next

        return head


class Solution_withhead(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val<val:
                cur = cur.next
                continue
            if p.next.val>val:
                p = dummy
            while p.next.val <val:
                p = p.next
            temp = cur.next
            cur.next = temp.next
            temp.next = p.next
            p.next = temp
        return dummy.next

def printList(head):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next


class Solution_sortarr(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        dummy = ListNode(0)
        while head != None:
            arr.append(head)
            head = head.next

        arr.sort(key = lambda x : x.val)
        curr = dummy
        for node in arr:
            curr.next = node
            curr = curr.next
        curr.next = None
        return dummy.next




def main():
    # values = [-1,5,7,4,0]
    values = [-1,5,6,3,4,0]
    values = [4,2,1,3]
    head = ListNode(values[0])
    cur = head
    for value in values[1:]:
        cur.next = ListNode(value)
        cur = cur.next
    printList(head)
    sol = Solution()
    sol.insertionSortList(head)

if __name__ == '__main__':
    main()
