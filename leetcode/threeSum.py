class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums)):
            target = -1*nums[i]
            for j in nums[i+1:]:
                dic[nums[j]]=j
            if two:
                sol = [nums[i],nums[two[0]+i+1],nums[two[1]+i+1]]
                sol.sort()
                if sol not in res:
                    res.append(sol)
        return res
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [i,dic[target - nums[i]]]
            dic[nums[i]]=i

def main():
    sol = Solution()
    x = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(x))


if __name__ == '__main__':
    main()
