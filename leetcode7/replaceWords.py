class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        for i,word in enumerate(words):
            for root in dict:
                # print(root,word[:len(root)])
                if root == word[:len(root)]:
                    words[i] = root
                    break
        return ' '.join(words)

class Solution(object):
    def replaceWords(self, worddict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        END = '#'
        trie = {} # 27th: whether it's an end
        for w in worddict:
            node = trie
            for ch in w:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node[END] = True
        output = []
        replaceDict = {}
        sentence = sentence.split(' ')
        for w in sentence:
            if not w in replaceDict:
                replaceDict[w] = w
                node = trie
                for idx, ch in enumerate(w):
                    if ch not in node:
                        break
                    if END in node[ch]:
                        replaceDict[w] = w[:idx+1]
                        break
                    node = node[ch]
            output.append(replaceDict[w])
        return ' '.join(output)

sol = Solution()
dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(sol.replaceWords(dict,sentence))
