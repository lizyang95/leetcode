class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left,right+1):
            testlist = list(str(i))
            print(testlist)
            if '0' in testlist:
                continue
            for j in range(len(testlist)):
                if i%int(testlist[j]):
                    break
                if j == len(testlist)-1:
                    res.append(i)
        return res


def main():
    sol = Solution()
    print(sol.selfDividingNumbers(1,22))

if __name__ == '__main__':
    main()
