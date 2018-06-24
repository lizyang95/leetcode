# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node
    def lowestCommonAncestorRecursive(self,root,p,q):
        node = root
        if not node:
            return node
        while node:
            if node.val > p.val and node.val > q.val:
                return self.lowestCommonAncestorRecursive(node.left,p,q)
            elif node.val < p.val and node.val < q.val:
                return self.lowestCommonAncestorRecursive(node.right,p,q)





def main():
    sol = Solution()
    root = [6,2,8,0,4,7,9,None,None,3,5]
    p = 2
    q = 4
    print(sol.lowestCommonAncestor(root,p,q))

if __name__ == '__main__':
    main()
