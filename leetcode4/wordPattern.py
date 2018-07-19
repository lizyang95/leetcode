class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        mapping = {}
        dest = set()
        if len(pattern) != len(words):
            return False
        for index,char in enumerate(pattern):
            if char in mapping:
                if mapping[char]!= words[index]:
                    return False
            else:
                if words[index] in dest:
                    return False
                mapping[char]=words[index]
                dest.add(words[index])
        return True
