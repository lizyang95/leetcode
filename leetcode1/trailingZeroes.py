class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = n-n%5
        if n ==0:
            return 0
        return n/5 + self.trailingZeroes(n/5)
