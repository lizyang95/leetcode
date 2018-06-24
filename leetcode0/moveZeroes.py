class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # zeros = 0
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         zeros += 1
        # if zeros == len(nums) or len(nums)==1:
        #     # print(nums)
        #     return
        # else:
        #     print(len(nums)-zeros)
        #     nums[:len(nums)-zeros]=[num for num in nums if num != 0]
        #     nums[len(nums)-zeros:] = [0 for i in range(zeros)]
        zero = 0
        for index in range(0,len(nums)):
            print(index,zero)
            if nums[index]!=0:
                nums[index],nums[zero]=nums[zero],nums[index]
                zero+=1
            print(nums)

def main():
    sol = Solution()
    nums = [0,1,0,3,12]
    # nums = [0,0]
    # nums = [0,0,1]
    # print(sol.moveZeroes(nums))
    sol.moveZeroes(nums)

if __name__ == '__main__':
    main()
