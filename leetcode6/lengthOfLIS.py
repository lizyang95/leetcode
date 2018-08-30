
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [nums[0]]
        for n in nums[1:]:
            if n > res[-1]:
                res.append(n)
            else:
                res.pop()
                res.append(n)
        print(res)
        return len(res)


sol = Solution()
nums =[4,10,4,3,8,9]
print(sol.lengthOfLIS(nums))
