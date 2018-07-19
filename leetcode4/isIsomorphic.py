class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t): return False
        ls=len(set(zip(s,t)))
        s_set=len(set(s))
        t_set=len(set(t))

        return t_set==s_set and t_set == ls

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        dest = set()
        #isIsometric = True
        for i, char in enumerate(s):
            if char in mapping:
                if mapping[char] != t[i]:
                        return False
            else:
                if t[i] in dest:
                    return False
                mapping[char] = t[i]
                dest.add(t[i])
        return True

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.translate(s)==self.translate(t)

    def translate(self,s):
        dic = {}
        res = ''
        for index,char in enumerate(s):
            if char not in dic:
                dic[char]=str(index)
        for char in s:
            res += dic[char]
        return res
        
