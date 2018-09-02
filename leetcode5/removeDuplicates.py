class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        writeto = 0
        count = 0
        if not nums:
            return 0
        if nums[0]==nums[-1]:
            return min(len(nums),2)
        last = nums[-1]
        for i,n in enumerate(nums):
            if n != last:
                last = n
                count = 1
                nums[writeto]=n
                writeto += 1
            elif count ==1:
                count += 1
                nums[writeto]=n
                writeto += 1
        return writeto








sol = Solution()
nums = [0,0,1,1,1,1,2,3,3]
print(sol.removeDuplicates(nums))
print(nums)
