class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1,len(nums)-1,2):
            tmp = nums[i+1]
            nums[i+1]=nums[i]
            nums[i]=tmp

class Solution(object):
    def wiggleSort(self, nums):
        for i in xrange(1, len(nums)):
            if (i % 2) ^ (nums[i] > nums[i - 1]):
                # ((i % 2 == 1) != (nums[i] > nums[i - 1]))
                # the if less is related to the index
                nums[i], nums[i - 1] = nums[i - 1], nums[i]


sol = Solution()
nums = [3,5,2,1,6,4]
sol.wiggleSort(nums)
print(nums)
