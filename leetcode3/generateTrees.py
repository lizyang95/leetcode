class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return [[]]
        return self.dfs(1, n+1)

    def dfs(self, start, end):
        if start == end:
            return None
        result = []
        for i in xrange(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i+1, end) or [None]:
                    node = TreeNode(i)
                    node.left, node.right  = l, r
                    result.append(node)
        return result

    def generateTrees(self, n):
        if not n:
            return []
        def generate(first, last):
            trees = []
            for root in range(first, last+1):
                for left in generate(first, root-1):
                    for right in generate(root+1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees += node,
            return trees or [None]
        return generate(1, n)


    def generateTrees_with_memo(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        memo = {}
        def helper(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            elif start == end:
                memo[(start, end)] = [TreeNode(start)]
                return memo[(start, end)]
            elif start > end:
                return [None]


            result = []
            for root in range(start, end+1):
                possible_left = helper(start, root-1)
                possible_right = helper(root+1, end)
                for left in possible_left:
                    for right in possible_right:
                        root_node = TreeNode(root)
                        root_node.left = left
                        root_node.right = right
                        result.append(root_node)

            memo[(start, end)] = result
            return result

        return helper(1, n)
