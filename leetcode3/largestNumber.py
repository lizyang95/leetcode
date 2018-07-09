class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        numsStr = [str(num) for num in nums]
        numsStr = sorted(numsStr,key=LargerNumKey)
        # print(numsStr)
        if set(numsStr) == set(['0']):
            numsStr = ['0']
        numstr = ''.join(numsStr)
        # print(numstr)
        return numstr

sol = Solution()
nums = [3,30,300]
print(sol.largestNumber(nums))
