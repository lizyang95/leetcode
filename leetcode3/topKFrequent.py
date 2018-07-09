class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections,heapq
        count = collections.Counter(nums)
        # print(count)
        heap = [(-val, key) for key, val in count.items()]
        # print(heap)
        heapq.heapify(heap)
        # print(heap)
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res

sol = Solution()
nums = [1,1,2,2,2,2]
k = 2
print(sol.topKFrequent(nums,k))
