class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        if len(string)==1:
            if string.isdigit():
                return float(string)
            else:
                return 0
        if not string:
            return 0
        for i,char in enumerate(string):
            if char!=' ':
                break
        if char!='-' and not char.isdigit():
            return 0
        for j,char in enumerate(string[i+1:]):
            print(char)
            if not char.isdigit():
                break
        end = i+j+1

        num = string[i:end]
        print(num)
        if '-' in num and '+' in num:
            return 0
        if(abs(float(num))>2147483648):
            return 2147483648 if float(num) > 0 else -1*2147483648
        return float(num)



def main():
    sol = Solution()
    string = '  -042a1'
    string = '-1'
    # string = '-+1'
    # string = "words and 987"
    # string = "4193 with words"
    print(sol.myAtoi(string))


if __name__ == '__main__':
    main()
