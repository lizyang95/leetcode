class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[int(len(nums)/2)]

        return sum([abs(num - median) for num in nums])
