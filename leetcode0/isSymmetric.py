# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return True
        queue = collections.deque([root])
        queue.append(root)
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if  t1.val != t2.val:
                return False

            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True

class recursiveSolution(object):
    def isSymmetric(self,root):
        return self.isMirror(root,root)

    def isMirror(self,root1,root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.isMirror(root1.right,root2.left) and self.isMirror(root1.left,root2.right)



def main():
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(sol.isSymmetric(root))

if __name__ == '__main__':
    main()
