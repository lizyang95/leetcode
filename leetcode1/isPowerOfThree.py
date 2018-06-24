class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        if n == 1:
            return True
        if n%3:
            return False
        return self.isPowerOfThree(n/3)  

def main():
    sol = Solution()
    n = 0
    print(sol.isPowerOfThree(n))

if __name__ == '__main__':
    main()
