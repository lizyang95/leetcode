class Solution(object):
    def longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [0 for j in xrange(n)]
        dp[n-1] = 1

        for i in xrange(n-1, -1, -1):   # can actually start with n-2...
            newdp = dp[:]
            newdp[i] = 1
            for j in xrange(i+1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j-1]
                else:
                    newdp[j] = max(dp[j], newdp[j-1])
            dp = newdp

        return dp[n-1]

    def longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for j in xrange(n)] for i in xrange(n)]

        for i in xrange(n-1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]
