class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if not s:
        #     return -1
        # counter = {char:0 for char in s}
        # for char in s:
        #     counter[char] += 1
        # for i,char in enumerate(s):
        #     if counter[char]==1:
        #         return i
        # return -1
        dict = {}
        for char in s:
            if char not in dict:
                dict[char]=1
            else:
                dict[char]=dict[char]+1

        for i in range(len(s)):
            char=s[i]
            if dict[char]==1:
                return i
        return -1

def main():
    sol = Solution()
    s = "aabbcc"
    print(sol.firstUniqChar(s))

if __name__ == '__main__':
    main()
