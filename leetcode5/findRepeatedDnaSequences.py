class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # temp = [s[i:i+10] for i in range(len(s)-9)]
        # from collections import Counter
        # counter = Counter(temp)
        # # print(counter)
        # return [string for string in counter if counter[string]>1]
        ans = set()
        seq = set()
        for i in xrange(len(s)-9):
            curSeq = s[i:i+10]
            if curSeq in seq:
                ans.add(curSeq)
            else:
                seq.add(curSeq)

        return list(ans)


sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(sol.findRepeatedDnaSequences(s))
