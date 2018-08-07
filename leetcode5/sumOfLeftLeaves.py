# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node and node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                stack.append(node.left)
            if node and node.right:
                stack.append(node.right)
        return res

class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root:
            if root.left:
                if root.left.left == None and root.left.right == None:
                    # has left leaf
                    return root.left.val + self.sumOfLeftLeaves(root.right)
            #else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        return 0
