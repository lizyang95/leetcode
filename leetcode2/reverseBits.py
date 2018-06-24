class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        string = "{0:032b}".format(n)[::-1]           # 32 bit unsigned num
        return int(string,2)

    def reverseBits(self, n):
        ans = 0
        for i in xrange(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans
