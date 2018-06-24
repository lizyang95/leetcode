class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in nums[1:]:
            result ^= i
        return result

class Solution(object):
    def singleNumber(self, nums):
        a= set(nums)
        a = sum(a)*3 -sum(nums)
        a = a/2
        return a


class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        for i in range(1,len(nums)-1):
            if nums[i-1]!=nums[i] and nums[i]!=nums[i+1]:
                return nums[i]
