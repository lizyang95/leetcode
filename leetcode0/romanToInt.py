class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        dictory1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        dictory2 = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        while i < len(s):
            if s[i:i+2] in dictory2:
                sum += dictory2[s[i:i+2]]
                i += 2
            else:
                sum += dictory1[s[i]]
                i += 1
        return sum


def main():
    sol = Solution()
    s = "MCMXCIV"
    s = 'LVIII'
    s = 'IX'
    print(sol.romanToInt(s))

if __name__ == '__main__':
    main()
