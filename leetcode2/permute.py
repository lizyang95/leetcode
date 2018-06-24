class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        i = 1
        while i < len(nums):



            i+=1



def main():
    sol = Solution()
    print(sol.permute([1,2,3]))

if __name__ == '__main__':
    main()
