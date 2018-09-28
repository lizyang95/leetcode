class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minPrice = prices[0]
        maxprofit = 0
        for price in prices:
            if minPrice > price:
                minPrice = price
            maxprofit = max(maxprofit,price - minPrice)
        return maxprofit

# with cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
class Solution(object):
    def maxProfit(self,prices):
        if not prices:
            return 0
        s0 = [0]*len(prices)
        s1 = [0]*len(prices)
        s2 = [0]*len(prices)

        s1[0] = -prices[0]
        s2[0] = -1
        for i in range(1,len(prices)):
            s0[i] = max(s0[i-1],s2[i-1])
            s1[i] = max(s1[i-1],s0[i-1]-prices[i])
            s2[i] = s1[i-1]+prices[i]
        return max(s0[-1],s2[-1])
