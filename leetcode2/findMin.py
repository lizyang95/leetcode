class Solution(object):
    def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
        N = len(nums)
        if(N == 1):
            return nums[0]
        low,high = 0,N-1

        while(low < high):
            mid = low + (high-low)/2
            if(nums[mid] < nums[high]):
                high = mid
            else:
                low = mid + 1

        return nums[low]
