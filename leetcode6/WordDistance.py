class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dictionary = {word:[] for word in words}
        for ind,word in enumerate(words):
            self.dictionary[word].append(ind)


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = self.dictionary[word1]
        index2 = self.dictionary[word2]
        mindistance = abs(index1[0]-index2[0])
        for i in index1:
            for j in index2:
                if abs(i-j)<mindistance:
                    mindistance = abs(i-j)
        return mindistance


words = ["practice", "makes", "perfect", "coding", "makes"]
map = WordDistance(words)
print(map.shortest('makes','coding'))
