class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        words.sort(key = lambda word:len(word))
        start = [word for word in words if len(word)==1]
        candidates = []
        for word in words:
            if word in start:
                candidates.append(word)
            else:
                for idx,candidate in enumerate(candidates):
                    if word[:-1]== candidate:
                        candidates.append(word)
        candidates.sort(key=lambda word:(len(word),word))
        last = candidates[-1]
        print(candidates)
        for i in range(len(candidates)-1,-1,-1):
            if len(candidates[i]) < len(last):
                return last
            last = candidates[i]
sol = Solution()
words = ['b',"a", "banana"]
print(sol.longestWord(words))
