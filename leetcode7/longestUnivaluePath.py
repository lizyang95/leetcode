class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        res = [0]
        def help(root, pre, res):
            if  not root.left and not root.right:
                if root.val == pre:
                    return 1
                else:
                    return 0
            left = right = 0
            if root.left:
                left = help(root.left, root.val, res)
            if root.right:
                right = help(root.right, root.val, res)
            res[0] = max(res[0], left+right)
            if root.val == pre:
                return 1+max(left, right)
            else:
                return 0
        return max(help(root, root.val-1, res), res[0])
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans
