class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = max(prices)
        profit = 0
        for i in range(len(prices)):
            if prices[i]<minPrice:
                minPrice = prices[i]
            else:
                profit = max(profit,prices[i]-minPrice)
        return profit

def main():
    sol = Solution()
    nums = [7,1,5,6,3,0]
    # nums = [6,4,3,1]
    print(sol.maxProfit(nums))

if __name__ == '__main__':
    main()
