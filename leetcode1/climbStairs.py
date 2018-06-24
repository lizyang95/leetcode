class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        pre = 2
        prepre = 1
        for i in range(3,n+1):
            pre,prepre = pre+prepre,pre
        return pre




def main():
    sol = Solution()

    print(sol.climbStairs(5))


if __name__ == '__main__':
    main()
