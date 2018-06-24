class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        dp = costs[0]
        for i in range(1,len(costs)):
            currRed, currBlue, currGreen = costs[i][0], costs[i][1], costs[i][2]
            preRed,preBlue,preGreen = dp
            dp = [
                min(preRed+currRed,preRed+currBlue,preRed+currGreen),
                min(preBlue+currRed,preBlue+currBlue,preBlue+currGreen),
                min(preGreen+currRed,preGreen+currBlue,preGreen+currGreen)
            ]
        return min(dp)

def main():
    sol = Solution()
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    # print(sol.judgeSquareSum(c))
    print(sol.minCost(costs))


if __name__ == '__main__':
    main()
