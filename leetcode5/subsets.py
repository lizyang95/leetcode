class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # classic case of DFS
        # Increment index by one so that you will get tree like this
        '''
        for 0 1 2 traversing will be like this
        []
        [1]
        [2, 1]
        [3, 2, 1]
        [3, 1]
        [2]
        [3, 2]
        [3]
        '''

        result = []
        nums = sorted(nums)
        self.dfs(result, 0, [], nums)
        return result

    def dfs(self, result, index, current_comb, nums):
        # Add current combination to result
        result.append(current_comb)
        for i in range(index, len(nums)):
            # go deeper with index 0 then return back then with index 1 then return back and then with index 2 and so on
            self.dfs(result,i+1,[nums[i]]+current_comb, nums)

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rl=[]
        self.backTracking(nums,0,[],rl)
        return rl

    def backTracking(self,nums,index,tl,rl):
        rl.append(tl)
        while index<len(nums):
            sl=tl+[nums[index]]
            index+=1
            self.backTracking(nums,index,sl,rl)

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        powerset = [[]]

        for num in nums:
            powerset = powerset + [subset +[num] for subset in powerset]

        return powerset
