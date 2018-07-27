# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        results = []
        cur_level_nodes = [root]
        next_level_nodes = []
        while len(cur_level_nodes) > 0:
            cur_level_vals = []
            for node in cur_level_nodes:
                cur_level_vals.append(node.val)
                if node.left: next_level_nodes.append(node.left)
                if node.right: next_level_nodes.append(node.right)
            results.append(cur_level_vals)
            cur_level_nodes = next_level_nodes
            next_level_nodes = []
        return results


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            tempq = []
            for node in queue:
                temp.append(node.val)
                if node.left:
                    tempq.append(node.left)
                if node.right:
                    tempq.append(node.right)

                queue = tempq
            res.append(temp)
        return res
