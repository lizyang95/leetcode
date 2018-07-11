class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        stack = []
        j = 0
        if not nums:
            if lower != upper:
                return [str(lower)+'->'+str(upper)]
            else:
                return [str(lower)]
        for i in range(lower,upper+1):
            # print(res)
            if j == len(nums):
                # print(stack)
                if nums[j-1]+1 == upper:
                    return res
                else:
                    res.append(str(nums[-1]+1) + '->' + str(upper))
                    return res
            if i == nums[j]:
                j += 1
                if len(stack)>1:
                    res.append(str(stack[0])+'->'+str(stack[-1]))
                    stack = []
                elif len(stack)==1:
                    res.append(str(stack[0]))
                    stack = []
            else:
                stack.append(i)
        if stack:
            if len(stack)==1:
                res.append(str(stack[0]))
            else:
                res.append(str(stack[0]+'->'+str(stack[-1])))
        return res





sol = Solution()
nums = [0, 1, 3, 50,99]
lower = 0
upper = 99
nums = [2147483647]
lower = 0
upper = 2147483647
print(sol.findMissingRanges(nums,lower,upper))
