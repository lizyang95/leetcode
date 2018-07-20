class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cumsum = [0]
        for x in nums:
            self.cumsum.append(x+self.cumsum[-1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cumsum[j+1] - self.cumsum[i]
