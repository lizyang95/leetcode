# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root,root)

    def isMirror(self,t1,t2):
        if t1==None and t2==None:
            return True
        if t1 == None or t2 == None:
            return False
        return (t1.val == t2.val) and self.isMirror(t1.right,t2.left) and self.isMirror(t1.left,t2.right)


    def isSymmetric_incursive(self,root):
        from collections import deque
        queue = deque([root,root])
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            if t1==None and t2==None:
                continue
            if t1==None or t2==None:
                return False
            if t1.val !=t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True
