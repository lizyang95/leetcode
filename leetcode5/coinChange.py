class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for j in range(len(coins)):
                if coins[j]<=i:
                    dp[i] = min(dp[i],dp[i-coins[j]]+1)
        # print(dp)
        if dp[amount]>amount:
            return -1
        else:
            return dp[amount]




sol = Solution()
coins = [1, 2, 5]
amount = 11
print(sol.coinChange(coins,amount))
