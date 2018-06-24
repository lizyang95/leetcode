import pdb
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        SubStr = []
        maxSubStr = []
        for i in range(len(s)):
            if s[i] in SubStr:
                SubStr = SubStr[SubStr.index(s[i])+1:len(SubStr)]
            SubStr.append(s[i])
            if len(SubStr)>len(maxSubStr):
                maxSubStr=SubStr
        # print(maxSubStr)
        return len(maxSubStr)

def main():
    sol = Solution()

    s = 'avaf'
    # s = 'abcdabcdbb'
    # s = 'bbbbb'
    # s = 'pwwkew'
    print(sol.lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()
