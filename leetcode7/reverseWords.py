class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        str[:] = list(' '.join(reversed(''.join(str).split(' '))))

    def reverseWords(self, s):
        # step 1: reverse the whole sentence
        self.reverse(s, 0, len(s) - 1)

        beg = 0
        for i in xrange(len(s)):
            # reverse each word
            if s[i] == ' ':
                self.reverse(s, beg, i-1)
                beg = i + 1
            elif i == len(s) -1:
                # reverse the last word, if there is only one word, this is th corner case
                self.reverse(s, beg, i)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords_withreversed(self, s):
    """
    :type s: a list of 1 length strings (List[str])
    :rtype: nothing
    """
        s.reverse()

        index = 0
        for i in range(len(s)):
            if s[i] == " ":
                s[index: i] = reversed(s[index: i])
                index = i + 1

        s[index: ] = reversed(s[index: ])


sol = Solution()
str = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
sol.reverseWords(str)
print(str)
