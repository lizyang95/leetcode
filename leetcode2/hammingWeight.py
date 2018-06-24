class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # print("{0:b}".format(n))
        # return "{0:b}".format(n).count('1')
        # return(str(bin(n)).count('1'))
        counter = 0
        while n:
            n &= (n - 1)
            counter += 1
        return counter

def main():
    sol = Solution()
    print(sol.hammingWeight(3))

if __name__ == '__main__':
    main()
