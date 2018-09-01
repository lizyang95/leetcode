class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        chars = list(set(s))
        memo = [[0]*len(chars)]
        dic = {char:0 for char in s}
        for char in s:
            dic[char]+=1
            memo.append([dic[char] for char in chars])
        print(memo)
        maxlen = 0
        for i in range(len(memo)):
            for j in range(i+1,len(memo)):
                count = [memo[j][m] - memo[i][m] for m in range(len(memo[0]))]
                if self.checkvalid(k,count) and j-i>maxlen:
                    maxlen = j-i
        return maxlen



    def checkvalid(self,k,count):
        for num in count:
            if num < k and num != 0:
                return False
        return True


sol= Solution()
s = "aaabb"
k = 2
print(sol.longestSubstring(s,k))
