class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        q = []
        preVal = -sys.maxint - 1
        cur = root

        while q or cur is not None:
            if cur is not None:
                q.append(cur)
                cur = cur.left
            else:
                check = q.pop()
                if preVal >= check.val:
                    return False
                preVal = check.val
                cur = check.right

        return True
