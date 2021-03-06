class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        start, end = 0, num

        while start <= end:
            mid = start + (end - start)//2

            if mid * mid == num:
                return True

            if mid * mid < num:
                start = mid + 1
            else:
                end = mid - 1

        return False
