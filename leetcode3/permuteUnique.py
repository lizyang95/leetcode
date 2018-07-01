class Solution(object):
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break              #handles duplication, avoid inserting a number before any of its duplication
            ans = new_ans
            # print(ans)
        return ans


def main():
    sol = Solution()
    print(sol.permuteUnique([1,1,2]))

if __name__ == '__main__':
    main()
