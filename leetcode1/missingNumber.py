class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) == len(nums)-1:
            return len(nums)
        # maximum = max(nums)
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
    def missingNumberHashSet(self,nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
    def missingNumberXOR(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing





def main():
    sol = Solution()
    nums = [0,1,2]
    nums = [9,6,4,2,3,5,7,0,1]
    print(sol.missingNumber(nums))

if __name__ == '__main__':
    main()
