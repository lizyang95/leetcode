class Solution(object):
  def findMissingRanges(self, A, lower, upper):
        result = []
        A.append(upper+1)
        pre = lower - 1
        for i in A:
           if (i == pre + 2):
               result.append(str(i-1))
           elif (i > pre + 2):
               result.append(str(pre + 1) + "->" + str(i -1))
           pre = i
        return result

        
    def helper(self, start, end):
        if start==end:
            return "{}".format(start)
        else:
            return "{}->{}".format(start,end)


nums = [0, 1, 3, 50, 75,99]
lower = 0
upper = 99
sol = Solution()
print(sol.findMissingRanges(nums,lower,upper))
