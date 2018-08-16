# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rightview = []
        leftview = []
        bottom = []
        queue = [root]
        while queue:
            newqueue = []
            for node in queue:
                
