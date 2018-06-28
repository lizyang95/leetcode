class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = float('inf')
        min2 = float('inf')
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:     # n lies between min1 and min2
                min2 = n
            if n >= max1:            # n is greater than max1, max2 and max3
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:   # n lies betweeen max1 and max2
                max3 = max2;
                max2 = n
            elif n >= max3:    # n lies betwen max2 and max3
                max3 = n


        return max(min1 * min2 * max1, max1 * max2 * max3)
        
