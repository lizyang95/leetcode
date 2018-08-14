import collections
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """

        if len(words1)!=len(words2):
            return False

        dic = collections.defaultdict(set)
        for w1,w2 in pairs:
            dic[w1].add(w2)
            dic[w2].add(w1)
            if w1 in dic:
                for w in dic[w1]:
                    dic[w].add(w2)
                    dic[w2].add(w)
            if w2 in dic:
                for w in dic[w2]:
                    dic[w].add(w1)
                    dic[w1].add(w)

        for i in range(len(words1)):
            if words1[i]==words2[i]:
                continue
            if words2[i] not in dic[words1[i]]:
                return False
        return True






sol = Solution()
words1 = ["great", "acting", "skills"]
words2 = ["fine", "painting", "talent"]
pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]
print(sol.areSentencesSimilarTwo(words1,words2,pairs))
