# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        maxloc = nums.index(max(nums))
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:maxloc])
        root.right = self.constructMaximumBinaryTree(nums[maxloc+1:])
        return root

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        stack = []
        for i in xrange(len(nums)):
            node = TreeNode(nums[i])
            while stack and stack[-1].val < node.val:
                node.left = stack.pop()

            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
