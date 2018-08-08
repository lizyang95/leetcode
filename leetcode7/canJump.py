class Solution(object):
    def canJump(self,nums):
        farthest=0
        for i in range(len(nums)):
            if i<=farthest and nums[i]+i>farthest:
                farthest=nums[i]+i
                # print (farthest)
        return farthest>=len(nums)-1
        
    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last=len(nums)-1 # the smallest index that can jump to the last index
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=last:
                last=i
        return last<=0

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        dp = [0]*len(nums)
        dp[0]=nums[0]
        for i,num in enumerate(nums[1:]):
            if i+1 <= dp[i]:
                dp[i+1] = max(i+1+nums[i+1],dp[i])
        return dp[-1]!=0


sol = Solution()
nums = [3,2,1,0,4]
nums = [2,3,1,1,4]
print(sol.canJump(nums))
