class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            # print(start,end)
            mid = (start + end)//2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                start = mid
                end = mid
                while 1:
                    if start == 0 or nums[start - 1] != target:
                        break
                    start -= 1
                while 1:
                    if end == len(nums)-1 or nums[end+1] != target:
                        break
                    end += 1
                return [start,end]
        return [-1,-1]


sol = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(sol.searchRange(nums,target))
