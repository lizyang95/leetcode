class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # dict = {}
        # for i in range(len(numbers)):
        #     if target-numbers[i] not in dict:
        #         dict[numbers[i]] = i
        #     else:
        #         res = [dict[target-numbers[i]]+1,i+1]
        #         return res
        d = {}

        for idx, num in enumerate(numbers):
            tmp = target - num
            if tmp in d:
                return [d[tmp] + 1, idx+1]
            d[num] = idx

def main():
    sol = Solution()
    numbers = [2,7,13,631]
    target = 9
    # print(sol.judgeSquareSum(c))
    print(sol.twoSum(numbers,target))


if __name__ == '__main__':
    main()
