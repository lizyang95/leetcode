class Solution(object):

    def isPalindrom(self,s):
        pass

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverseds = s[::-1]
        max = 0




def main():
    sol = Solution()
    s = 'abab'
    print(sol.longestPalindrome(s))

if __name__ == '__main__':
    main()
