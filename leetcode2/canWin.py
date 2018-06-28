class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in xrange(len(s)-1):
            if s[i]=='+' and s[i+1]=='+' and not self.canWin(s[:i]+'--'+s[i+2:]): return True
        return False

class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def helper(s):
            if s in memo:
                return memo[s]
            for i in range(len(s) - 1):
                if s[i:i + 2] == '++' and not helper(s[:i] + '--' + s[i + 2:]):
                    memo[s] = True
                    return True

            memo[s] = False
            return False
        memo = {}
        return helper(s)
