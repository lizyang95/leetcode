class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n = len(nums)
        # nums.sort()
        # for i in range(1,n):
        #     if nums[i-1]==nums[i]:
        #         rep = nums[i]
        # missing = rep + (1+n)*n/2 - sum(nums)
        # return [rep,missing]


        n=len(nums)
        sum1=sum(nums)
        nums=set(nums)
        sum2=sum(nums)
        rep=sum1-sum2
        mis=(1+n)*n/2-sum2
        return [rep,mis]



sol = Solution()
nums = [1,4,2,2]
print(sol.findErrorNums(nums))
