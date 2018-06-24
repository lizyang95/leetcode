class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # digits = []
        # origin_n = n
        # while 1:
        #     print(digits)
        #     digits.append(n%10)
        #     n = int(n/10)
        #     if n==0:
        #         break
        # sum = 0
        # for i in digits:
        #     sum += i**2
        # if sum == 1:
        #     return True
        # elif sum==origin_n:
        #     return False
        # else:
        #     return self.isHappy(sum)
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True


def main():
    sol = Solution()
    print(sol.isHappy(2))

if __name__ == '__main__':
    main()
