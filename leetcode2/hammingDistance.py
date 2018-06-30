class Solution(object):
    def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x^y).count('1')

class Solution(object):
    def hammingWeight(self, n):
        counter = 0
        while n != 0:
            counter += 1
            n &= (n - 1)
        return counter

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return self.hammingWeight(x ^ y)


class Solution(object):
    def hammingDistance(self,x,y):
        ans = 0
        while x or y:
          ans += (x % 2) ^ (y % 2)
          x /= 2
          y /= 2
        return ans
