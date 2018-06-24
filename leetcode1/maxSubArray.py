class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = nums[0]
        # print(dp)
        maxsum = dp
        for i in range(1,len(nums)):
            dp = max(dp+nums[i],nums[i])
            maxsum = max(maxsum,dp)
            # print(dp)
        return maxsum

def main():
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sol.maxSubArray(nums))


if __name__ == '__main__':
    main()
