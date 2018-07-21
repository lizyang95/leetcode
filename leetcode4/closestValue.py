# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        cur = root
        while cur:
            if abs(cur.val - target) < abs(closest - target):
                closest = cur.val
            if cur.val == target:
                return cur.val
            elif cur.val > target:
                cur = cur.left
            else:
                cur = cur.right

        return closest
