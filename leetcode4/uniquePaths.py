class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n == 1:
            return 1
        return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n == 1:
            return 1
        import math
        return math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1))

sol = Solution()
print(sol.uniquePaths(4,4))
