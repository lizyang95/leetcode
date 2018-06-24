class Solution(object):
    def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
        lis = list(range(1, len(nums)+1))
        for num in nums:
        lis[num - 1] = 0

            i = 0
            while i < len(lis):
                if lis[i] == 0:
                    del lis[i]
                else:
                    i += 1

            return lis

def main():
    sol = Solution()
    # s = 'abobe'
    s = 'oe'
    print(sol.reverseVowels(s))

if __name__ == '__main__':
    main()
