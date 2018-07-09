class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        t=s.split(" ")
        m=[]
        for x in t:
            m.append(x[::-1])
        return " ".join(m)


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        ret = []
        for word in l:
            # wl = word.split()
            # wl = wl[::-1]
            # print(wl)
            ret.append("".join(reversed(word)))
        return " ".join(ret)
