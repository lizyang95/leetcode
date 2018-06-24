class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        queue = [0]
        ls = len(s)
        lenList = [l for l in set(map(len, wordDict))]
        visited = [0 for _ in range(0, ls + 1)]
        while queue:
            start = queue.pop(0)
            for l in lenList:
                if s[start:start + l] in wordDict:
                    if start + l == ls:
                        return True
                    if visited[start + l] == 0:
                        queue.append(start + l)
                        visited[start + l] = 1
        return False

    def wordBreakDP(self, s, dict):
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True

        return dp[-1]



def main():
    sol = Solution()
    s = "aaaaaaa"
    wordDict = ["aaaa", "aaa"]
    print(sol.wordBreak(s,wordDict))

if __name__ == '__main__':
    main()
