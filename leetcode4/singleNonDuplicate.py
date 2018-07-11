import pdb
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: nums[int]
        :rtype: int
        """
        low, high = 0 , len(nums)-1
        while (low<high):
            # pdb.set_trace()
            mid = (low + high) >> 1
            if (nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]):
                return nums[mid]
            if (mid%2 ==1 and nums[mid]==nums[mid-1]):
                low = mid+1
            elif (mid%2 ==0 and nums[mid]==nums[mid+1]):
                low = mid+1
            else:
                high = mid -1
        return nums[low]

sol = Solution()
nums = [1,1,3,3,5,4,4,8,8]
print(sol.singleNonDuplicate(nums))
