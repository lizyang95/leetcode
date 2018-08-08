class Solution(object):
    def lexicalOrder(self, n):
        res = [0] * n
        cur = 1
        for i in range(n):
            res[i] = cur
            if cur * 10 <= n:
                cur = cur * 10
            else:
                if cur >= n:
                    cur = cur / 10
                cur += 1
                while cur % 10 == 0:
                    cur = cur / 10
        return res

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def lexicalRange( limit, start, end, result ):
            for i in xrange( start, end ):
                if i > limit:
                    break
                result.append( i )
                nextStart   = i * 10
                if nextStart <= limit:
                    lexicalRange( limit, nextStart, nextStart + 10, result )

            return result

        result              = []
        lexicalRange( n, 1, 10, result )

        return result


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        strings = [str(i) for i in range(1,n+1)]
        strings.sort()
        res = [int(string) for string in strings]
        return res



sol = Solution()
print(sol.lexicalOrder(13))
