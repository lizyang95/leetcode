class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1. get the start index of non-increasing sequence from tail
        # 2. swap
        # 3. sort the non-increasing
        if not nums: return nums
        l = len(nums)
        i, j = l - 2, l - 1
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = sorted(nums[i+1:])


# ////////////////////////////////////////////////////////////
def reverse(a, lo, hi):
    while lo < hi:
        a[lo], a[hi] = a[hi], a[lo]
        lo += 1
        hi -= 1


class Solution_withoutsort(object):
    def nextPermutation(self, a):
        n = len(a)
        for j in range(n-1, 0, -1):
            if a[j] > a[j-1]:
                k = j
                break
        else:
            reverse(a, 0, n-1)
            return
        for j in range(n-1, k-1, -1):
            if a[j] > a[k-1]:
                i = j
                break
        else:
            raise ValueError(a)
        a[i], a[k-1] = a[k-1], a[i]
        reverse(a, k, n-1)
sol = Solution()
# nums = [1,2,5]
nums = [1]
sol.nextPermutation(nums)
print(nums)
