class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = 0
        # i = 0
        # while i < len(nums)-1:
        #     # print(i,nums[i],nums[i+1])
        #     if nums[i]==nums[i+1]:
        #         res += 1
        #         nums.pop(i)
        #         i -= 1
        #     print(nums)
        #     i += 1
        # return res
        i = -1
        j = 0
        while j < len(nums):
            if i==-1 or nums[j]!=nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        # print(nums)
        return i+1



def main():
    sol = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    # nums = [1,1,2]
    print(sol.removeDuplicates(nums))

if __name__ == '__main__':
    main()
