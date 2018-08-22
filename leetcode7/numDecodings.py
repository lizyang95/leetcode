class Solution:
    def numDecodings(self, s):
        if s[0] == "0": return 0
        dp1 = dp2 = 1
        for i in range(1, len(s)):
            if s[i] == "0" and (s[i - 1] == "0" or s[i - 1] >= "3"): return 0  # only '10', '20' is valid
            dp1, dp2 = [dp2, dp1] if s[i] == "0" else [dp2, dp2 + dp1] if "10" <= s[i -1: i + 1] <= "26" else [dp2, dp2]
             # '01 - 09' is not allowed
        return dp2
# A digit from index 1 have three condition
# 
# '?10' or '?20' this can only divide into '10' or '20' , f(n) = f(n-2)
#
# '?26' this can divide into '6' or '26', f(n) = f(n-2)+f(n-1)
#
# '?09', '?27' this can only divide into '9' or '7' , f(n) = f(n-1)

sol = Solution()
print(numDecodings('226'))
