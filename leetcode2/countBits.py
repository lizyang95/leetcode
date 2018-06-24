class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        n = num + 1
        bits = [0] * n

        for i in range(1, n):
            bits[i] = bits[i & (i-1)] + 1

        return bits

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num ==0:
            return [0]

        d = [0]* (num+1)
        d[0] = 0
        d[1] =1


        for i in range (2, num+1):
            d[i] = d[i//2] + (i % 2)

        return d
            
