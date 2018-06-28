class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        # f[i] means maximum product that can be achieved ending with i
        # g[i] means minimum product that can be achieved ending with i
        n = len(nums)
        f, g = [0] * n, [0] * n
        f[0], g[0] = nums[0], nums[0]
        res = nums[0]
        for i in xrange(1, n):
            f[i] = max(nums[i], nums[i] * f[i-1], nums[i] * g[i-1])
            g[i] = min(nums[i], nums[i] * f[i-1], nums[i] * g[i-1])
            res = max(res, f[i])
        return res

    def maxProductOptimized(self, nums):
        if not nums: return 0
        r = nums[0]
        imax, imax_pre, imin, imin_pre = r, r, r, r
        for i in xrange(1, len(nums)):
            imax = max(nums[i], imax_pre * nums[i], imin_pre * nums[i])
            imin = min(nums[i], imax_pre * nums[i], imin_pre * nums[i])
            imax_pre = imax
            imin_pre = imin
            r = max(imax, r)
        return r
        
    def maxProduct(self,nums):
        maximum=big=small=nums[0]
        for n in nums[1:]:
            big, small=max(n, n*big, n*small), min(n, n*big, n*small)
            maximum=max(maximum, big)
        return maximum
