class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid+1
        return left


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # return A.index(max(A))

        left = 0
        right = len(A)-1
        mid = (left+right)//2

        while (A[mid]-A[mid-1])*(A[mid]-A[mid+1]) < 0:
            if A[mid] < A[mid-1]: # peak on the left
                right = mid-1
                mid = (left+right)//2
            else: # peak on the right
                left = mid+1
                mid = (left+right)//2

        return mid

sol = Solution()
nums =  [0,2,1,0]
print(sol.peakIndexInMountainArray(nums))
