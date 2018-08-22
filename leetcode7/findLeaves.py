from collections import defaultdict


class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        depth_layers = defaultdict(list)
        self.dfs(depth_layers, root)
        return [leaves for depth, leaves in sorted(depth_layers.items())]

    def dfs(self, depth_layers, root):
        if not root:
            return 0

        cur_depth = 1 + max(self.dfs(depth_layers, root.left), self.dfs(depth_layers, root.right))
        depth_layers[cur_depth].append(root.val)
        return cur_depth

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if (not root.right) and (not root.left):
            return [[root.val]]
        res = []

        while root and (root.right or root.left) :
            stack = []
            leave = []
            if root.left:
                stack.append((root,root.left,'left'))
            if root.right:
                stack.append((root,root.right,'right'))
            while stack:
                prenode,node,pos = stack.pop()
                if (not node.left) and (not node.right):
                    leave.append(node.val)
                    if pos == 'left':
                        prenode.left = None
                    if pos == 'right':
                        prenode.right = None
                else:
                    if node.left: stack.append((node,node.left,'left'))
                    if node.right: stack.append((node,node.right,'right'))
            res.append(leave)
        res.append([root.val])
        return res


            
