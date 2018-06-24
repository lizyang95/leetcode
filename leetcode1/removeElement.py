class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        for i in range(len(nums))[::-1]:
            if nums[i] == val:
                del nums[i]

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while 1:
            if i >= len(nums):
                break
            if nums[i]==val:
                del nums[i]
                continue
            i += 1
        return len(nums)
