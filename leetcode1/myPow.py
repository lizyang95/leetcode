class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x

        pRes = self.myPow(x,n/2)

        if n %2 == 0:
            return pRes * pRes
        else:
            return pRes * pRes * x
