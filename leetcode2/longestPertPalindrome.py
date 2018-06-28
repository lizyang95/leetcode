import collections
class Solution:
    def longestPalindrome(self, s):
        ans = 0
        for v in collections.Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

def main():
    sol = Solution()
    s = "aaabbbccc"
    print(sol.longestPalindrome(s))

if __name__ == '__main__':
    main()
