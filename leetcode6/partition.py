class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -=1
            return True
        res = []
        def dfs(path, start):
            if start >= len(s):
                res.append(path)
            else:
                for i in range(start, len(s)):
                    if isPalindrome(start, i):
                        dfs(path+[s[start:i+1]], i+1)
        dfs([], 0)
        return res
                
