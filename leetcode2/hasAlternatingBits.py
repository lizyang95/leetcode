class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prelable = n&1
        n >>= 1
        while n:
            lable = n&1
            if prelable == lable:
                return False
            n >>= 1
            prelable = lable
        return True
