class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data, res = {}, []
        for i in nums:
            data[i] = data[i] + 1 if i in data else 1
        bucket = [[] for i in xrange(len(nums)+1)]
        for key in data:
            bucket[data[key]].append(key)
        for content in bucket:
            content.sort()
        for i in xrange(len(bucket)-1, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                break
        return res[:k]
