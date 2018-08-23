class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        neg = 0
        if numerator * denominator < 0:
            neg = 1
        n = abs(numerator)
        d = abs(denominator)

        ans = n // d
        rem = n % d
        res = ""
        hMap = {}
        count = 0
        while rem:
            rem *= 10
            num = rem // d
            if rem in hMap:
                idx = hMap[rem]
                res = res[:idx] + '(' + res[idx:] + ')'
                break
            hMap[rem] = count
            count += 1
            res += str(num)
            rem = rem % d
        res = str(ans) + '.' + res if len(res) > 0 else str(ans)
        return '-' + res if neg else res



sol = Solution()
print(sol.fractionToDecimal(1,2))
