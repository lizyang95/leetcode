class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        if num%4:
            return False
        return self.isPowerOfFour(num/4)


class Solution(object):
    def isPowerOfFour(self, num):
        # mask = 1431655765       # using XOR on all power of 4 -> 1010101010101010101010101010101  =  1431655765
        mask = int('0b1010101010101010101010101010101', 2)
        maxx = 2**31

        return num > 0 and maxx%num==0 and mask&num == num
