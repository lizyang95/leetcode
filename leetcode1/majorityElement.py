class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={nums[i]:0 for i in range(len(nums))}
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
        for key in hashmap:
            if hashmap[key]>int(len(nums)/2):
                return key
        return
        
