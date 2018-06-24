class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = [prices[i+1]-prices[i] if prices[i+1]-prices[i] > 0 else 0 for i in range(len(prices)-1)]
        return sum(diff)


def main():
    sol = Solution()
    nums = [7,1,5,3,6,4]
    nums =  [1,2,3,4,5]
    # nums = [2,2,5,5]
    print(sol.maxProfit(nums))

if __name__ == '__main__':
    main()
