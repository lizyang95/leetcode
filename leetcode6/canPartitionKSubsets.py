class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 1: return True
        if sum(nums) % k != 0: return False
        target = sum(nums) // k
        nms = []
        for i in nums:
            if i == target:
                k -= 1
            elif i > target:
                return False
            else:
                nms.append(i)

        def dfs(nums, k, curSum, i):
            if k <= 1:
                return True
            elif curSum == target:
                return dfs(nums, k - 1, 0, 0)
            else:
                for i in xrange(i, len(nums)):
                    if chosen[i] == 0 and curSum + nums[i] <= target:
                        chosen[i] = 1
                        rst = dfs(nums, k, curSum + nums[i], i + 1)
                        if rst: return True
                        chosen[i] = 0
                return False

        nms.sort(reverse= True)
        chosen = [0] * len(nums)
        return dfs(nms, k, 0, 0)

sol = Solution()
nums = [4, 3, 2, 3, 5, 2, 1,2,2,2,1]
k = 4
print(sol.canPartitionKSubsets(nums,k))
