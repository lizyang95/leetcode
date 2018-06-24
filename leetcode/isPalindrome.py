class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x<0:
        #     return False
        # string = str(x)[::-1]
        # # print(string)
        # if len(string)==1:
        #     return True
        # if int(string)==x:
        #     return True
        # else:
        #     return False
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False



def main():
    sol = Solution()
    x = -1221
    # x = 10
    # x = -1
    print(sol.isPalindrome(x))


if __name__ == '__main__':
    main()
