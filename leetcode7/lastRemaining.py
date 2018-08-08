class Solution:
    def lastRemaining(self, n):
        head, left, step, remaining = 1, 1, 1, n
        while remaining > 1:
            if left or remaining % 2: head += step
            left = 1 - left
            step *= 2
            remaining //= 2
        return head

# https://leetcode.com/problems/elimination-game/discuss/87119/JAVA:-Easiest-solution-O(logN)-with-explanation

sol = Solution()
print(sol.lastRemaining(9))
