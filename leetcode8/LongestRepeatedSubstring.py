class Solution(object):
    def lcp(self,s,t):
        n = min(len(s),len(t))
        for i in range(n):
            if s[i]!=t[i]:
                return s[:i]
        return s[:n]


    def lrs(self,s):
        suffixes = []
        n = len(s)
        for i in range(len(s)):
            suffixes.append(s[i:n])
        print(suffixes)
        suffixes.sort()
        print(suffixes)
        lrString = ''
        for i in range(n-1):
            commonString = sol.lcp(suffixes[i],suffixes[i+1])
            if len(commonString)>len(lrString):
                lrString = commonString
        return lrString

sol = Solution()
s = "bananac"
print(sol.lrs(s))
