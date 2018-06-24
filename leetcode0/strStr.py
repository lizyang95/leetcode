class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)

        if len(haystack) < len(needle):
            return -1
        if haystack == needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1

def main():
    sol = Solution()
    haystack = "mississippi"
    needle = "pi"
    print(sol.strStr(haystack,needle))

if __name__ == '__main__':
    main()
