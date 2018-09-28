class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp = {pos : set() for pos in stones}
        dp[0].add(0)
        for i in xrange(0, len(stones) - 1):
            for step in dp[stones[i]]:
                for k in xrange(step-1, step+2):
                    if k > 0 and stones[i] + k in dp:
                        dp[stones[i] + k].add(k)
        return len(dp[stones[-1]]) > 0
