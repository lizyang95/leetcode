
class Solution_expand(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        mx = ''
        for i in range(n):
            mx  = max(mx,self.middle_to_end(i, i, s), self.middle_to_end(i, i+1, s),  key=len)

        return mx

    def middle_to_end(self, l, r, s):

        while l>=0 and r<len(s) and s[l] == s[r]:
            l += -1
            r += 1
        return s[l+1:r]

        return mx


class Solution_self(object):
    def expandeven(self,s,i):
        diff = 0
        res = s[i]
        while True:
            if i-diff >=0 and i+diff <len(s):
                if s[i-diff]==s[i+diff]:
                    res = s[i-diff:i+diff+1]
                    diff += 1
                else:
                    break
            else:
                break
        return res

    def expandodd(self,s,i):
        diff = 0
        if i+2<=len(s):
            res = s[i:i+2]
            if res[0]!= res[1]:
                return res[0]
        res = s[i:i+2]
        while True:
            # print(res,diff)
            if i-diff >=0 and i+diff+2 <=len(s):
                if s[i-diff]==s[i+diff+1]:
                    res = s[i-diff:i+diff+2]
                    diff += 1
                else:
                    break
            else:
                break
        return res

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0 or len(s)==1:
            return s
        if len(s)==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        maxlen = 0
        res = ''
        for i in range(0,len(s)):
            evenres = self.expandeven(s,i)
            oddres = self.expandodd(s,i)
            # print(evenres,oddres)

            if len(evenres)>maxlen:
                res = evenres
                maxlen = len(res)
            if len(oddres)>maxlen:
                res = oddres
                maxlen = len(res)
        return res

def main():
    sol = Solution()
    s = 'babab'
    s = 'cssa'
    s = 'a'
    s = 'bb'
    s = 'ccd'
    s = 'abb'
    s = 'aaaa'
    s = '"tattarrattat"'
    print(sol.longestPalindrome(s))


if __name__ == '__main__':
    main()
