class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # k: distance
        # t: value diff
        



sol = Solution()
nums = [1,5,9,1,5,9]
k = 2
t = 3
print(sol.containsNearbyAlmostDuplicate(nums,k,t))
