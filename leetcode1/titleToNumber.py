class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = [::-1]
        sum = 0
        for i in range(len(s)):
            sum += (26**i)*ord(s[i])
        return sum
            
