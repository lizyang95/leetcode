
class  Solution(object):
     def  licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        no_dash = S.upper().replace('-', '')
        n = len(no_dash)
        new = []
        i = (K if n%K == 0 else n%K)
        new.append(no_dash[:i])

        while i < n:
            new.append(no_dash[i:i+K])
            i += K
        return '-'.join(new)


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        stack = []
        res = []
        for char in S:
            if char.isdigit():
                stack.append(char)
            elif char!="-":
                stack.append(char.upper())
        print(stack)
        num = 0
        while stack:
            if num < K:
                res.append(stack.pop())
                num += 1
            else:
                res.append("-")
                num = 0
        return ''.join(res)[::-1]






sol = Solution()
S = "5F3Z-2e-9-w"
K = 4
print(sol.licenseKeyFormatting(S,K))
