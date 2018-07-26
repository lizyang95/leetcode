class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves = 0
        for i in range(1,len(nums)):
            diff = moves + nums[i] - nums[i-1]
            nums[i] += moves
            moves += diff
        return moves



sol = Solution()
nums = [1,2,3]
print(sol.minMoves(nums))
