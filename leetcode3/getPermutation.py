class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = map(str, range(1, 10))
        k -= 1
        factor = 1
        for i in range(1, n):
            factor *= i
        res = []
        for i in reversed(range(n)):
            print("factor:",factor,'res:',res,'nums:',nums,'k:',k)
            res.append(nums[k / factor])
            nums.remove(nums[k / factor])
            if i != 0:
                k %= factor
                factor /= i
        return "".join(res)


from math import factorial
class Solution_another(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = [i for i in xrange(1, n+1)]
        while n-1 >= 0:
            num, k = k/factorial(n-1), k % factorial(n-1)
            if k > 0:
                res.append(str(nums[num]))
                nums.remove(nums[num])
            else:
                res.append(str(nums[num-1]))
                nums.remove(nums[num-1])

            n -= 1

        return ''.join(res)


def main():
    sol = Solution()
    print(sol.getPermutation(4,3))

if __name__ == '__main__':
    main()
