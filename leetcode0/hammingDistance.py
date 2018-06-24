class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # xl = self.toBinary(x)
        # yl = self.toBinary(y)
        #
        # print(xl)
        # print(yl)
        #
        # if len(xl)<len(yl):
        #     sl = xl
        #     ll = yl
        # else:
        #     sl = yl
        #     ll = xl
        # dis = sum(ll[0:len(ll)-len(sl)])
        # ll = ll[len(ll)-len(sl):]
        # dis += sum([1 if sl[i] !=  ll[i]  else 0 for i in range(len(sl))])
        #
        # return dis
        return bin(x ^ y).count('1')

    # def toBinary(self,x):
    #     res = []
    #     while x > 0:
    #         res.append(x%2)
    #         x = int(x/2)
    #     return res[::-1]
    #


def main():
    sol = Solution()
    x = 14
    y = 2
    print(sol.hammingDistance(x,y))

if __name__ == '__main__':
    main()
