class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list = ['a','e','i','o','u','A','E','I','O','U']
        left = 0
        right = len(s)-1
        string = [char for char in s]
        while left < right:
            while s[left] not in list and left < right:
                left += 1
            while s[right] not in list and left < right:
                right -= 1
            string[left] = s[right]
            string[right] = s[left]
            left += 1
            right -= 1
        return ''.join(string)



def main():
    sol = Solution()
    # s = 'abobe'
    s = 'oe'
    print(sol.reverseVowels(s))

if __name__ == '__main__':
    main()
