class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False

        # binary and map
        # from collections import defaultdict
        # import bisect as bi
        # idx = defaultdict(list)
        # for i, c in enumerate(t):
        #     idx[c].append(i)
        # prev = 0
        # for i, c in enumerate(s):
        #     j = bi.bisect_left(idx[c], prev)
        #     if j == len(idx[c]): return False
        #     prev = idx[c][j] + 1
        # return True


class Solution(object):
    def isSubsequence(self, s, t):
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True

sol = Solution()
s = "abc"
t = "ahbgdc"
s = 'ab'
t = ''
s = "leeeeetcode"
# t = 'leeetcode'
# s = 'bcs'
# t = 'ubcs'
print(sol.isSubsequence(s,t))
