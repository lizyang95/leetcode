# bottom up:
# minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];

# since the row minpath[k+1] would be useless after minpath[k] is computed, we can simply set minpath as a 1D array
# For the kth level:
# minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i]


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return
        res = triangle[-1]
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]

    # Modify the original triangle, bottom-up
    def minimumTotal_Constant_space(self, triangle):
        if not triangle:
            return
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]


sol = Solution()
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(sol.minimumTotal(triangle))
