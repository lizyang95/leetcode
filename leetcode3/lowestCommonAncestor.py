# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor_recursive(self, root, p, q):
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor_incursive(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        l=root
        while (p.val-l.val)*(q.val-l.val)>0:
            if p.val>l.val:
                l=l.right
            else:
                l=l.left
        return l

    # while root:
    #     if root.val > p.val and root.val > q.val:
    #         root = root.left
    #     elif root.val < p.val and root.val < q.val:
    #         root = root.right
    #     else:
    #         return root
