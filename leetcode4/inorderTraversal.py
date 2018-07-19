class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                root = tmpNode.right
        return res

class Solution_dfs(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node,l=[]):
            if node.left:
                dfs(node.left,l)
            l.append(node.val)
            if node.right:
                dfs(node.right,l)
            return l
        l = dfs(root)
        return min([abs(l[i]-l[i+1] for i in range(len(l)-1))])
