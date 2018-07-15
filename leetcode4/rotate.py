class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tmp = nums[:]
        for i in range(len(nums)):
            nums[i] = tmp[(i-k)%len(nums)]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n=len(nums)
        nums[:]=nums[n-k:]+nums[:n-k]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k > 0:
            for i in range(len(nums)-k):
                nums.append(nums.pop(0))



sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
nums = [-1]
k = 2
sol.rotate(nums,k)
print(nums)
