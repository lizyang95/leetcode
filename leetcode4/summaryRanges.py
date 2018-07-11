class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # res = []
        # if not nums:
        #     return []
        # if len(nums)==1:
        #     return [str(nums[0])]
        # nextrange = 0
        # start = nums[0]
        # end = nums[0]
        # for i in range(1,len(nums)):
        #     if nums[i]-nums[i-1]==1 or(nextrange == 1 and nums[i]-start ==1):
        #         end = nums[i]
        #         nextrange = 0
        #     else:
        #         if start != end:
        #             res.append(str(start)+'->'+str(end))
        #         else:
        #             res.append(str(start))
        #         start = nums[i]
        #         end = nums[i]
        #         nextrange = 1
        # if end == nums[-1]:
        #     if start != end:
        #         res.append(str(start)+'->'+str(end))
        #     else:
        #         res.append(str(start))
        # if end != nums[-1]:
        #     res.append(str(nums[-1]))
        # return res

        res=[]
        stack=[]
        for num in nums:
            if not stack:
                stack.append(num)
            elif num-1==stack[-1]:
                stack.append(num)
            else:
                if len(stack)==1:
                    res.append(str(stack.pop()))
                    stack.append(num)
                else:
                    res.append(str(stack[0])+"->"+str(stack[-1]))
                    stack=[num]
        if stack:
            if len(stack)==1:
                res.append(str(stack.pop()))
            else:
                res.append(str(stack[0])+"->"+str(stack[-1]))

        return res

        
sol = Solution()
nums = [0,1,2,4,5,7]
# nums = [0,2,4,6,8,9]
print(sol.summaryRanges(nums))
