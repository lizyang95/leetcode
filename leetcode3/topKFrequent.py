class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {num:0 for num in nums}
        for num in nums:
            dic[num] += 1
        frequencydic = {value:[] for value in dic.values()}
        for key,value in dic.items():
            frequencydic[value].append(key)
        print(frequencydic)
        frequencylist = list(frequencydic.values())
        frequencylist.sort()
        ans = []
        while len(ans)<k:
            frequency = frequencylist[-1]
            for num in frequencydic[frequency]:
                ans.append(num)
                frequencylist.pop()

        return ans

sol = Solution()
nums = [1,2]
k = 2
print(sol.topKFrequent(nums,k))
