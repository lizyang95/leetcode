# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        counter = 0
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                counter += 1
                root = node.right
                if counter == k:
                    return node.val

class Solution(object):
    def kthSmallest(self, root, k):
        stack, cur = [], root
        i = 0
        while i < k and (stack or cur):
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            i += 1
            if i == k:
                return node.val
            cur = node.right
