class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnts = [0]*32
        for num in nums:
            i = 0
            while num:
                cnts[i] += num&1
                num >>= 1
                i += 1

        return sum([cnt*(len(nums)-cnt) for cnt in cnts])
