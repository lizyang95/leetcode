# top-down approach, O(n*logn)
def sortedListToBST_recursive(self, head):
    if not head:
        return
    if not head.next:
        return TreeNode(head.val)
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    root = TreeNode(slow.next.val)
    root.right = self.sortedListToBST(slow.next.next)
    slow.next = None
    root.left = self.sortedListToBST(head)
    return root

# convert linked list to array
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        tree = []
        while head:
            tree.append(head.val)
            head = head.next
        root = self.constructTree(tree)
        return root

    def constructTree(self, tree):
        if not tree:
            return
        mid = len(tree)/2
        root = TreeNode(tree[mid])
        root.left = self.constructTree(tree[:mid])
        root.right = self.constructTree(tree[mid+1:])
        return root

# bottom-up approach, O(n)
def sortedListToBST_bottom_up(self, head):
    l, p = 0, head
    while p:
        l += 1
        p = p.next
    return self.convert([head], 0, l-1)

def convert(self, head, start, end):
    if start > end:
        return None
    mid = (start + end) >> 1
    l = self.convert(head, start, mid-1)
    root = TreeNode(head[0].val)
    root.left = l
    head[0] = head[0].next
    root.right = self.convert(head, mid+1, end)
    return root
