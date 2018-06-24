class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ['{','[','(']
        right = ['}',']',')']
        for char in s:
            if char in left:
                stack.append(char)
            elif not stack:
                print("empty stack")
                return False
            elif stack.pop()!=left[right.index(char)]:
                return False
        if stack:
            return False
        return True

def main():
    sol = Solution()
    s = '{{{}}'
    print(sol.isValid(s))

if __name__ == '__main__':
    main()
