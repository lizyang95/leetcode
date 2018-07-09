class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import collections
        counts = collections.Counter(nums)
        lenlimit = int(len(nums)/3)
        res = []
        for key,value in counts.items():
            if value > lenlimit:
                res.append(key)
        return res
        
