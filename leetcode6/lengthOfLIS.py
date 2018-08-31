class Solution(object):
    # dp[x] = max(dp[x], dp[y] + 1) 其中 y < x 并且 nums[x] > nums[y]
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = [1] * size
        for x in range(size):
            for y in range(x):
                if nums[x] > nums[y# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        ]:
                    dp[x] = max(dp[x], dp[y] + 1)
        return max(dp) if dp else 0


# 维护一个单调序列
# 遍历nums数组，二分查找每一个数在单调序列中的位置，然后替换之。


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[x])
            else:
                dp[low] = nums[x]
        return len(dp)


sol = Solution()
nums =[4,10,4,3,8,9]
print(sol.lengthOfLIS(nums))
