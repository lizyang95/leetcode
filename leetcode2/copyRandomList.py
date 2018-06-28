class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return

        cur = head
        while cur:
            newNode = RandomListNode(cur.label)
            newNode.next = cur.next
            newNode.random = cur.random
            cur.next = newNode
            cur = cur.next.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        second = cur = head.next
        while cur.next:
            head.next = cur.next
            head = head.next
            cur.next = head.next
            cur = cur.next

        head.next = None
        return second

# http://www.cnblogs.com/zuoyuan/p/3745126.html

    # using dictionary
    def copyRandomList(self, head):
        if not head:
            return
        cur, dic = head, {}
        # copy nodes
        while cur:
            dic[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = head
        # copy random pointers
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[head]
