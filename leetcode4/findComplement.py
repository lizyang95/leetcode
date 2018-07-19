class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num

class Solution(object):
    def findComplement(self, num):

        if num == 0:
            ans = "0"
        ans = ''
        while num:
            if num & 1 == 1:
                ans = "1" + ans
            else:
                ans = "0" + ans
            num //= 2
        ans = list(ans)
        for i, q in enumerate (ans):
            if q == "0":
                ans[i] = "1"
            if q == "1":
                ans[i] = "0"
        return int("".join(ans), 2)    
