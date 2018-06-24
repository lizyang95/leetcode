class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # if not a and not b:
        #     return
        # if not a:
        #     return b
        # if not b:
        #     return a
        #
        # extra = '0'
        # res = ''
        # a = a[::-1]
        # b = b[::-1]
        #
        # if len(a)<len(b):
        #     short = a
        #     long = b
        # else:
        #     short = b
        #     long = a
        #
        # for i in range(len(short)):
        #     sum = int(a[i]) + int(b[i]) + int(extra)
        #     res += str(sum%2)
        #     extra = str(int(sum/2))
        #
        # for i in range(len(long)-len(short)):
        #     sum = int(long[len(short)+i]) + int(extra)
        #     res += str(sum%2)
        #     extra = str(int(sum/2))
        #
        # if int(extra):
        #     res += str(extra)
        # return res[::-1]


        sum = int(a, 2) + int(b, 2)
        return bin(sum)[2:]

def main():
    sol = Solution()
    a = '1010'
    b = '1011'
    print(sol.addBinary(a,b))

if __name__ == '__main__':
    main()
