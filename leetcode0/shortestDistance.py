class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        loc1 = []
        loc2 = []
        for i in range(len(words)):
            if words[i]==word1:
                loc1.append(i)
            if words[i]==word2:
                loc2.append(i)
        # print(loc1,loc2)

        minlen = len(words)
        for i in range(len(loc1)):
            for j in range(len(loc2)):
                # print(loc1[i],loc2[j])
                if abs(loc1[i]-loc2[j])<minlen:
                    minlen = abs(loc1[i]-loc2[j])

        return minlen



class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        minDis = len(words)
        i1, i2 = float('inf'), float('inf')
        for i in xrange(len(words)):
            if words[i] == word1:
                i1 = i
                minDis = min(minDis, abs(i1 -i2))
            elif words[i] == word2:
                i2 = i
                minDis = min(minDis, abs(i1 -i2))
        return minDis
