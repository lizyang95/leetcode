# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def findSum(node):
            if not node:
                return 0
            l = findSum(node.left)
            r = findSum(node.right)
            self.ans += abs(l-r)
            return l+r+node.val
        findSum(root)
        return self.ans
