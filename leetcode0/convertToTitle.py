class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # code = 64+i  i in range(1,27)
        list = []
        while int(n/26):
            if n%26:
                list.append(n%26)
                n = int(n/26)
            else:
                list.append(26)
                n = int((n-26)/26)
        if n:
            list.append(n)
        list = list[::-1]

        s = ''
        for i in range(len(list)):
             s += chr(64+list[i])
        return s





def main():
    sol = Solution()
    # n = 29
    n = 701
    print(sol.convertToTitle(n))

if __name__ == '__main__':
    main()
