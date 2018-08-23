class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        out = float('inf')
        if word1 == word2:
            last = -float('inf')
            for i, w in enumerate(words):
                if w == word1:
                    out = min(out, i - last)
                    last = i
        else:
            locs = [-float('inf'), -float('inf')]
            for i, w in enumerate(words):
                if w == word1:
                    out = min(out, i - locs[1])
                    locs[0] = i
                elif w == word2:
                    out = min(out, i - locs[0])
                    locs[1] = i
        return out
