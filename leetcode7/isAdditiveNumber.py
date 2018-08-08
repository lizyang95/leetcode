class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num)<3:
            return False
        


num = "112358"
sol = Solution()
print(sol.isAdditiveNumber(num))
