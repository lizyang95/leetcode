class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums.reverse()
        firstK = nums[:k]
        last = nums[k:]
        firstK.reverse()
        last.reverse()
        nums[:k] = firstK
        nums[k:] = last



sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
sol.rotate(nums,k)
print(nums)
