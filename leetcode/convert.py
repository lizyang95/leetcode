class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # res = ['']*numRows
        # mod = (numRows-1)*2
        # if mod ==0:
        #     return s
        # for i in range(len(s)):
        #     if i%mod <= numRows-1:
        #         res[i%mod].append(s[i])
        #     else:
        #         res[mod-i%mod].append(s[i])
        # returnStr = ''
        # for i in range(len(res)):
        #     res[i] = ''.join(res[i])
        #     returnStr += res[i]
        # return returnStr
        line = ['']*numRows
        # print(line)
        row, step = 0 , 1
        if numRows == 1 or numRows >= len(s):
            return s
        for ch in s:
            line[row] += ch
            row += step
            if row == 0 or row == numRows-1:
                step *= -1

        return ''.join(line)

def main():
    sol = Solution()
    s = 'PAYPALISHIRING'
    # numRows = 3
    numRows = 4
    print(sol.convert(s,numRows))


if __name__ == '__main__':
    main()
