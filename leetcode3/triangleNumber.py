class Solution(object):

    def twoSum(self, A, n):
        i = 0
        j = len(A) -1
        count =0
        while i< j:
            if A[i] + A[j] > n:
                count += j-i
                j-=1
            else:
                i+=1
        return count

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return 0
        nums.sort()
        count = 0
        for i in range(2,len(nums)):
            count += self.twoSum(nums[:i],nums[i])

        return count


def main():
    sol = Solution()
    nums = [2,2,3,4]
    print(sol.triangleNumber(nums))

if __name__ == '__main__':
    main()
