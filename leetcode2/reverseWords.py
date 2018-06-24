class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return ' '.join(reversed(s.split()))


        words = s.split(' ')
        stack = []
        for word in words:
            if  word:
                stack.append(word)
        res = ''
        while stack:
            word = stack.pop()
            res += (word + ' ')
        return res[:-1]

def main():
    sol = Solution()
    print(sol.reverseWords('sky  is blue'))

if __name__ == '__main__':
    main()
