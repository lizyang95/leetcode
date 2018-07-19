class Solution(object):

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        string1 = 'qwertyuiop'
        string2 = 'asdfghjkl'
        string3 = 'zxcvbnm'
        res = []
        for word in words:
            if len(word)==1:
                res.append(word)
                continue
            origin = word
            word = word.lower()
            for string in [string1,string2,string3]:
                if word[0] in string:
                    break
            # print(string)
            for i in range(1,len(word)):
                if word[i] not in string:
                    break
            if i == len(word)-1 and word[i] in string:
                res.append(origin)
        return res

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_upper, row_mid, row_low = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        ans = []

        for word in words:
            w = set(word.lower())
            if w.issubset(row_upper) or w.issubset(row_mid) or w.issubset(row_low):
                ans.append(word)
        return ans

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l1, l2, l3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        return [i for i in words if any(set(i.lower()) <= j for j in [l1, l2, l3])]
