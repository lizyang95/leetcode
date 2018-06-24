class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        res = [1] * n

        for i in range(1, n):
            print(res)
            res[i] = res[i-1] * nums[i-1]
        print(res)

        back = 1
        for i in range(n-2, -1, -1):
            print("back")
            print(back)
            back *= nums[i+1]
            res[i] *= back
            print('res')
            print(res)

        return res

def main():
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4,5]))

if __name__ == '__main__':
    main()
