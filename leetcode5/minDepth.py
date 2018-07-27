class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if root.left is None:
            return right + 1
        elif root.right is None:
            return left + 1
        else:
            return min(left, right) + 1

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        frontier = [root]
        # out is the depth of frontier
        out = 1
        while frontier:
            nxt = []
            for u in frontier:
                if u.left != None: nxt.append(u.left)
                if u.right != None: nxt.append(u.right)
                if u.left == None and u.right == None:
                    return out
            frontier = nxt
            out += 1
