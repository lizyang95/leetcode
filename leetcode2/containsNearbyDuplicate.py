class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # dict = {num:[] for num in nums}
        # for i,num in enumerate(nums):
        #     dict[num].append(i)
        #
        # # print(dict)
        # for idxlist in dict.values():
        #     for i in range(len(idxlist)-1):
        #         if idxlist[i+1]-idxlist[i]<=k:
        #             return True
        #
        # return False
        #
        if not nums or k<0 or len(nums)==len(set(nums)):
            return False
        dic ={}
        for i,v in enumerate(nums):
            if v in dic and i - dic[v]<=k:
                return True
            dic[v] = i
        return False
