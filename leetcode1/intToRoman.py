class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str = ''
        dictory1 = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        values = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        while num>0:
            for i in values[::-1]:
                print(num,i)
                if num >= i:
                    str += dictory1[i]
                    num -= i
                    # print(str)
                    break

        return str


class Solution_faster(object):
    def intToRoman(self, num):
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]

def main():
    sol = Solution()
    print('hello world')
    print(sol.intToRoman(20))


if __name__ == '__main__':
    main()
