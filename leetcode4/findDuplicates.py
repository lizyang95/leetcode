class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        memo = set()
        res = []
        for num in nums:
            if num not in memo:
                memo.add(num)
            else:
                res.append(num)
        return res


# using the input array itself as a hash to store which numbers have been seen before
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res
