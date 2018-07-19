class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n==0:
            return 1
        more = 9 * math.factorial(9)/math.factorial(10-n)
        return self.countNumbersWithUniqueDigits(n-1) + more
        

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        n = 1, uni_count = 10
        n = 2, digit = 1, uniq_count = 10
               digit = 2, total_count = 9*10 = 90, repeat_count = 9, unique count = 90 - 9 + 10 = 91
                          total_number = 99+1=100 - 9 = 91
               digit = 3, total_count = 9 * 10 * 10 = 900, repeat =
        n = 3
        make a dictionary
        suppose n is really large the answer is always the same
        9 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 10
        """
        prev = 9
        res = [10]
        for i in xrange(9,0,-1):
            prev = prev * i
            res.append(prev)
        # print res: 10, 81, ...
        ans = [1]
        cum = 0
        for i in res:
            cum = cum+i
            ans.append(cum)
        if n > 10:
            n = 10
        #print ans # 10, 91, ...
        return ans[n]
