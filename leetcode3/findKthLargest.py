class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        count = {num:nums.count(num) for num in nums}
        heap = [(-key,val) for key,val in count.items()]
        heapq.heapify(heap)
        cnt = 0
        while cnt < k:
            item = heapq.heappop(heap)
            cnt += item[1]
        return -item[0]




sol = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
# nums = [3,2,1,5,6,4]
# k = 2
print(sol.findKthLargest(nums,k))
