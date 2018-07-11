class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        i = 1
        divisors = [1]
        while 1:
            if i*i>num:
                print(divisors)
                return num == sum(set(divisors))
            i += 1
            if num%i == 0:
                divisors.append(i)
                divisors.append(num/i)
                


sol = Solution()
print(sol.checkPerfectNumber(3021377))
