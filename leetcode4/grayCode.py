# When n = 2, the sequence is
# 00 -> 01 -> 11 -> 10
# If you want to extend it to n=3 directly without modifying old part, there are only two possible sequence, and they are not hard to find out.
#
# 000 -> 001 -> 011 -> 010 -> 110 -> 111 -> 101 -> 100
#
# 000 -> 001 -> 011 -> 010 -> 110 -> 100 -> 101 -> 111
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # if n ==0:
        #     return [0]
        # ret = [0,1]
        # for i in range(1,n):
        #     ret = ret + [pow(2,i) + ret[x] for x in range(len(ret)-1,-1,-1)]
        # return ret

        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
        return results


def main():
    sol = Solution()
    print(sol.grayCode(2))

if __name__ == '__main__':
    main()
