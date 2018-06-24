class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n ==1:
            return True
        if n == 0:
            return False
        while n != 2:
            if n%2:
                return False
            n = n/2
        return True

def main():
    sol = Solution()
    n = 0
    print(sol.isPowerOfTwo(n))

if __name__ == '__main__':
    main()
