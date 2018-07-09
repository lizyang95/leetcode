class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # import collections
        # ransomset = set(ransomNote)
        # magset = set(magazine)
        # if (ransomset | magset)!=magset:
        #     return False
        #
        # ransomdic = collections.Counter(ransomNote)
        # magdic = collections.Counter(magazine)
        #
        # for key,value in ransomdic.items():
        #     if value > magdic[key]:
        #         return False
        # return True

        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True



sol = Solution()
ransomNote = 'a'
magazine = 'b'
print(sol.canConstruct(ransomNote,magazine))
