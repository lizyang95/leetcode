class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestSize = 0
        longestStart = 0

        dp = [[0] * (len(s)) for i in range(len(s))]
        for index, value in enumerate(s):
            start,end = self.checkOddPal(s,index)
            longestSize,longestStart = self.update(start,end,longestSize,longestStart)
            start,end = self.checkEvenPal(s,index)
            if start == end:
                longestSize,longestStart = self.update(start,end,longestSize,longestStart)
        return s[longestStart:longestSize+longestStart+1]

    def _longest_common_substring(self,s1,s2):
       m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
       longest, x_longest = 0, 0
       for x in range(1, 1 + len(s1)):
           for y in range(1, 1 + len(s2)):
               if s1[x - 1] == s2[y - 1]:
                   m[x][y] = m[x - 1][y - 1] + 1
                   if m[x][y] > longest:
                       longest = m[x][y]
                       x_longest = x
               else:
                   m[x][y] = 0
       return s1[x_longest - longest: x_longest]

def main():
    sol = Solution()

    # s = 'babad'
    s = 'cbbd'
    # s = 'abacdfgdcaba'
    # s = ''

    print(sol.longestPalindrome(s))


if __name__ == '__main__':
    main()
