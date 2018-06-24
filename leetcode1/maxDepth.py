# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_second(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        depth = self.recurse_node(root, 1)
        return depth

    def recurse_node(self, node, depth):
        if not node:
            return depth-1
        left_depth = self.recurse_node(node.left, depth+1)
        right_depth = self.recurse_node(node.right, depth+1)

        if left_depth > right_depth:
            return left_depth
        else:
            return right_depth

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
