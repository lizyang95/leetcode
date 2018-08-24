class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if A == []: return
        p0 = 0; p2 = len(A) - 1; i = 0
        while i <= p2:
            if A[i] == 2:
                A[i], A[p2] = A[p2], A[i]
                p2 -= 1
            elif A[i] == 0:
                A[i], A[p0] = A[p0], A[i]
                p0 += 1
                i += 1
            else:
                i += 1

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Using Lomuto's partition algorithm
        # store value for each iteration
        # In-place one pass solution O(n) O(1)
        # No swap required
        # [0, i) are 0's
        # [i, j) are 1's
        # [j, k) are 2's
        i, j = 0, 0
        for k in range(len(nums)):
            cur = nums[k]   # store value
            nums[k] = 2 # make color blue
            if cur < 2: # if red or white
                nums[j] = 1 # make white
                j += 1
            if cur == 0:
                nums[i] = 0
                i += 1




sol = Solution()
nums = [2,0,2,1,1,0]
sol.sortColors(nums)
print(nums)
