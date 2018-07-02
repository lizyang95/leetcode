class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = []
        stack = []
        for index, char in enumerate(s):
            # print(index,char)
            if index%(2*k)<k:
                stack.append(char)
            else:
                while stack:
                    res.append(stack.pop())
                res.append(char)
        while stack:
            res.append(stack.pop())

        return ''.join(res)

        
class Solution(object):
    def reverseStr(self, s, k):
        k2 = 2*k
        x = ''
        for i in range(0, len(s),k2):
            x +=s[i:k+i][::-1]+s[k+i:k2+i]

        return x

def main():
    sol = Solution()
    s = 'abcd'
    k = 4
    print(sol.reverseStr(s,k))

if __name__ == '__main__':
    main()
