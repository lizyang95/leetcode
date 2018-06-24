class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # digit = 0
        # for i in range(len(digits)):
        #     digit += 10**i * digits[len(digits)-i-1]
        # res = []
        # digit += 1
        # while digit != 0:
        #     res.append(digit%10)
        #     digit = int(digit/10)
        # return res[::-1]
        over = 1
        res = []
        i = len(digits)-1
        while i >= 0:
            res.append((digits[i]+over)%10)
            over = int((digits[i]+over)/10)
            i -= 1
        if over:
            res.append(1)
        return res[::-1]


def main():
    sol = Solution()
    # digits = [4,3,2]
    digits = [9]
    print(sol.plusOne(digits))

if __name__ == '__main__':
    main()
