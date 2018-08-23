# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            newqueue = []
            rowvalues = []
            for node in queue:
                rowvalues.append(node.val)
                if node.left: newqueue.append(node.left)
                if node.right: newqueue.append(node.right)
            res.append(max(rowvalues))
            queue = newqueue
        return res
