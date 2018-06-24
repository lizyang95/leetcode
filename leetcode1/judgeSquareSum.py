class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        d=int(math.sqrt(c))
        for i in range(d+1):
            if math.sqrt(c-math.pow(i,2)).is_integer():
                return True
        return False


def main():
    sol = Solution()
    c = 5
    # print(sol.judgeSquareSum(c))
    print(sol.isSquareRoot(8))


if __name__ == '__main__':
    main()
