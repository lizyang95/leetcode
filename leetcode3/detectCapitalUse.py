class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word[1:].islower() or word.isupper() or len(word)==1

        
sol = Solution()
word = 'AlaG'
print(sol.detectCapitalUse(word))
