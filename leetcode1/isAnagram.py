class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # l = 'abcdefghijklmnopqrstuvwxyz'
        # for i in l:
        #     if(s.count(i) != t.count(i)):
        #         return False
        # return True
        if len(s) != len(t):
            return False
        return all(s.count(c)==t.count(c) for c in string.ascii_lowercase)
