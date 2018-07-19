class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        nums = list(s)
        permutes = self.permuteUnique(nums)
        for permute in permutes:
            string = ''.join(permute)
            if string == string[::-1]:
                res.append(string)
        return res


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
    s = 'abc'
    print(sol.generatePalindromes(s))

if __name__ == '__main__':
    main()
