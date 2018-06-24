class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # string = [char for char in s]
        # for char in t:
        #     if char not in string:
        #         return char
        #     string.pop(string.index(char))
        for c in t:
            if t.count(c) > s.count(c):
                return c

def main():
    sol = Solution()
    s = 'abcde'
    t = 'aabcde'
    print(sol.findTheDifference(s,t))

if __name__ == '__main__':
    main()
