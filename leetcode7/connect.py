# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        q = collections.deque([root])
        nextlvl = []
        while q:
            node = q.popleft()
            if node and node.left:
                nextlvl.append(node.left)

            if node and node.right:
                nextlvl.append(node.right)

            nextnode = q[0] if q else None
            if node: node.next = nextnode

            if not q:
                q = collections.deque(nextlvl)
                nextlvl = []
# use BFS
# to use a queue to store all node in a same level
# for each node in the queue, we connect the node to it's next, and add its children to the queue
import collections
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        if root != None:
            q = deque()
            q.append(root)
            while q:
                count = len(q)
                for i in range(0,count):
                    cur = q.popleft()
                    if i != 0:
                        node.next = cur
                        node = cur
                    else:
                        node = cur
                    if cur.left != None:
                        q.append(cur.left)
                    if cur.right != None:
                        q.append(cur.right)


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            cur = tmp = TreeLinkNode(0)
            while root:
                if root.left:
                    cur.next = root.left
                    cur = root.left
                if root.right:
                    cur.next = root.right
                    cur = root.right
                root = root.next
            root = tmp.next
