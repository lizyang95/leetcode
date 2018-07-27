class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root: return 0
        q = [root]
        res = []
        while q:
            curSum = 0
            nq = []
            for node in q:
                curSum += node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            res.append(1.0*curSum/(len(q)))
            q = nq
        return res

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level = [root]
        ans = []
        while len(level):
            sub = 0.0
            next_level = []
            for l in level:
                sub += l.val
                if l.left:
                    next_level.append(l.left)
                if l.right:
                    next_level.append(l.right)
            ans.append(sub/len(level))
            level = next_level
        return ans
