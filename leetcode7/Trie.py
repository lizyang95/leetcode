class Trie(object):
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.is_word = False

    def insert(self,word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]
        node.is_word = True

    def search(self,word):
        node = self
        for letter in word:
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]
        return node.is_word

    def startsWith(self,prefix):
        node = self
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        t = self.head
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        dic = self.head
        for w in word:
            if w in dic:
                dic = dic[w]
            else:
                return False
        if '#' in dic:
            return True
        else:
            return False



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        dic = self.head
        for w in prefix:
            if w in dic:
                dic = dic[w]
            else:
                return False
        return True
