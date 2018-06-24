class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if not s:
        #     return True
        # ls = ''
        # for i in range(len(s)):
        #     if s[i].isalpha():
        #         ls += s[i].lower()
        #     if s[i].isdigit():
        #         ls += str(s[i])
        # rls = ls[::-1]
        # print(ls,rls)
        # return rls==ls

        s = s.lower()
        s = filter(str.isalnum, str(s))
        # ''.join([i for i in s if i.isalpha() or i .isdigit()])
        return s == s[::-1]


def main():
    sol = Solution()
    s = '0P'
    print(sol.isPalindrome(s))


if __name__ == '__main__':
    main()
