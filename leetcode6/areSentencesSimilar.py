class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        similars = collections.defaultdict(set)
        for w1, w2 in pairs:
            similars[w1].add(w2)
            similars[w2].add(w1)
        for w1, w2 in zip(words1, words2):
            if w1 != w2 and w2 not in similars[w1]:
                return False
        return True



sol = Solution()
words1 = ["great"]
words2 = ["great"]
pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]
pairs = []
print(sol.areSentencesSimilar(words1,words2,pairs))
