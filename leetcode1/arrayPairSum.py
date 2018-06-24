class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        return sum(sorted(nums)[::2])


        nums.sort()
        # print(nums)
        sum = 0
        for i in range(len(nums)):
            if not i%2:
                sum += nums[i]
        return sum
