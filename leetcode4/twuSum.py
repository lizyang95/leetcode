class Solution(object):
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
        # return res

def main():
    sol = Solution()
    # nums = [2, 7, 11, 15]
    # target = 9
    # target = 6
    # nums = [3,3]
    nums = [3,2,4]
    target = 6
    print(sol.twoSum(nums,target))


if __name__ == '__main__':
    main()
