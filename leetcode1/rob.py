class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        # if len(nums)==1:
        #     return nums[0]
        # if len(nums)==2:
        #     return max(nums)
        # if len(nums)==3:
        #     return max(nums[0]+nums[2],nums[1])
        # dp = nums[0],max(nums[:2]),max(nums[0]+nums[2],nums[1])
        # for i in range(3,len(nums)):
        #     dp = dp[1],dp[2],max(dp[2],dp[1]+nums[i],dp[0]+nums[i])
        #     # print(dp)
        # return max(dp)
        pre, cur = 0, 0
        for n in nums:
            pre, cur = cur, max(pre+n, cur)
        return cur

def main():
    sol = Solution()
    # nums = [2,1,1,2]
    nums = [2,7,9,3,1]
    # nums = [1,3,1,4,100]
    print(sol.rob(nums))


if __name__ == '__main__':
    main()
