class Solution(object):
# consider the first element and the last element as -inf
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(float('-inf'))
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i]>nums[i+1]:
                return i
        return 0

class Solution_logn(object):
    # uses the intution that if the left neighbor is greater than the middle
     # element then the peak will lie on the left side otherwise the peak will lie on the right side
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) -1

        while left < right:
            mid = left + (right-left)/2
            if nums[mid] > nums[mid+1]:
                right  = mid
            else:
                left = mid+1

        return left

    def findPeakElement(self, nums):
        # considering the boundary
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
                return mid;
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1



sol = Solution()
nums =  [1,2,1,3,5,6,4]
nums = [1,2,3,3,5,6,7][::-1]
print(sol.findPeakElement(nums))
