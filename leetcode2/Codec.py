class Codec:

    def __init__(self):
        self.hashmap = {}
        self.length = 0


    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl not in hashmap.values:
            self.hashmap[self.length] = longUrl

        


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """


# Your Codec object will be instantiated and called as such:
url = https://leetcode.com/problems/design-tinyurl
codec = Codec()
print(codec.decode(codec.encode(url)))
