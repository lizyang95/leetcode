class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import collections
        queue = collections.deque()
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        queue.append(n)
        cnt = 0
        while queue:
            # print(queue)
            cnt += 1
            tmp = set()
            for x in queue:
                for y in squares:
                    if x == y:
                        return cnt
                    if x<y:
                        break
                    tmp.add(x-y)
            queue = tmp
        return cnt


class Solution_math(object):
    def is_square(self, n):
        tmp = (int)(math.sqrt(n))
        return tmp**2 == n

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # The result is 4 if and only if n can be written in the
        # form of 4^k*(8*m + 7). Please refer to
        # Legendre's three-square theorem.
        while n % 4 == 0: #n % 4 == 0
            n >>= 2

        if n % 8 == 7: #n % 8 == 7
            return 4


        if self.is_square(n):
            return 1

        # Check whether 2 is the result.
        sqrt_n = (int)(math.sqrt(n))
        for i in range(1, sqrt_n+1):
            if self.is_square(n-i**2):
                return 2

        return 3

class Solution_DP(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [sys.maxint]*(n+1)
        dp[0] = 0
        for i in xrange(n+1):
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i-j**2]+1, dp[i])
                j += 1
        return dp[n]

sol = Solution()
print(sol.numSquares(7168))
