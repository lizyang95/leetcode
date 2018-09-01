class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Iterative approach:
        stack = []
        stack.append(s)

        ans = 0
        while stack:
            s = stack.pop()
            for c in set(s):
                if s.count(c) < k:
                    stack.extend([z for z in s.split(c)])
                    break
            else:
                ans = max(ans, len(s))

        return ans 

sol= Solution()
s = "aaabb"
k = 2
print(sol.longestSubstring(s,k))
