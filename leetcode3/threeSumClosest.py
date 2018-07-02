class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = 0
        nums.sort()
        while True:
            res = self.threeSum(nums,target+diff)
            if res:
                return target+diff
            res = self.threeSum(nums,target-diff)
            if res:
                return target-diff
            diff += 1





    def threeSum(self, nums,n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums.sort()
        result,visited = set(),{}
        for i in xrange(len(nums)-2):
            table,target = {},n-nums[i]
            if nums[i] not in visited:
                for j in xrange(i+1,len(nums)):
                    if nums[j] not in table:    table[target - nums[j]] = j
                    else:   result.add((nums[i],target-nums[j],nums[j]))
                visited[nums[i]] = 1
        return list(result)



def main():
    sol = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    print(sol.threeSumClosest(nums,target))

if __name__ == '__main__':
    main()
