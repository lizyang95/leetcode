class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)


    def isSameTree_dfs(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p,q)]
        while stack:
            node1,node2 = stack.pop()
            if not node1 and not node2:
                continue
            if node1 == None or node2 == None:
                return False
            if node1.val != node2.val:
                return False
            stack.append((node1.right,node2.right))
            stack.append((node1.left,node2.left))

        return True

    def isSameTree_bfs(self,p,q):
        queue = [(p, q)]
        while queue:
            node1, node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True
