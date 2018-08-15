# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        from collections import deque
        queue = [root]
        while queue:
            newqueue = []
            rightnode = queue[-1]
            if rightnode: res.append(rightnode.val)
            for node in queue:
                if node and node.left: newqueue.append(node.left)
                if node and node.right: newqueue.append(node.right)
            queue = newqueue
        return res


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = [(root, 1)]
        res = []

        while queue:
            temp = []
            for node, height in queue:
                if len(res) < height:
                    res.append(node.val)
                if node.right:
                    temp.append((node.right, height+1))
                if node.left:
                    temp.append((node.left, height+1))
            queue = temp

        return res
        
