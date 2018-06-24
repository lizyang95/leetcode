class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if x >0:
        #     x = str(x)
        #     x = x[::-1]
        #     if int(x)>=2**31-1:
        #         return 0
        #     return int(x)
        # elif x == 0:
        #     return 0
        # else:
        #     x = str(x)
        #     x = x[::-1]
        #     x = x[0:len(x)-1]
        #     if int(x)>=2**31:
        #         return 0
        #     return -1*int(x)
        st = str(abs(x))
        st = st[::-1]
        if x > 0:
            x = int(st)
        else:
            x = -int(st)

        if abs(x) > 2**31:
            return 0
        else:
            return x


def main():
    sol = Solution()
    # nums = [2, 7, 11, 15]
    # target = 9
    # target = 6
    # nums = [3,3]
    # x = 234
    x = -234
    # x = 120
    print(sol.reverse(x))


if __name__ == '__main__':
    main()
