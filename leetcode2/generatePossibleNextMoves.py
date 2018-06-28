class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if not s:
            return []

        ret = []
        for i in xrange(1, len(s)):
            if s[i] == "+" and s[i-1] == "+":
                ret.append(s[:i-1] + "--" + s[i+1:])
        return ret
