class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {char:s.count(char) for char in s}
        values = [value%2 for value in dict.values()]
        return sum(values)<=1


class Solution_counter(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        table = collections.Counter(s)
        cnt = 0
        for i in table:
            if table[i]%2 != 0:
                cnt += 1
            if cnt > 1:
                return False
        return True
