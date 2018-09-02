class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        accsum = []
        for n in nums:
            sum += n
            accsum.append(sum)
        res = len(nums)
        if sum(nums)<s:
            return 0
        if sum(nums)==s:
            return res
        for i,n in enumerate(accsum):
            index = self.search(accsum,i,n+s)
            if index!=-1:
                res = min(res,index-i)
        return res

    def search(self,nums,startind,target):
        lo = startind
        hi = len(nums)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if mid == len(nums)-1:
                if nums[mid]



sol = Solution()
s = 7
nums = [2,3,1,2,4,3]
print(sol.minSubArrayLen(s,nums))
