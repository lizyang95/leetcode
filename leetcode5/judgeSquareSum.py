class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        hi = int(math.sqrt(c))
        lo = 0
        while lo <= hi:
            cur = lo * lo + hi * hi
            if cur == c:
                return True
            elif cur > c:
                hi -= 1
            else:
                lo += 1
        return False

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0: return True
        i = 0
        squares = set()
        while i*i <=c:
            num = c - i*i
            squares.add(i*i)
            if num in squares:
                return True
            i += 1
        return False
