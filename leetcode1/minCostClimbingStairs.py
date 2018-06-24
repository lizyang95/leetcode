class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        # f1 = f2 = 0
        # for x in reversed(cost):
        #     f1, f2 = x + min(f1, f2), f1
        # return min(f1, f2)
        if len(costs) in (0, 1): return 0
        min_cost0, min_cost1 = costs[0], costs[1]
        for cost in costs[2:]:
            min_cost0, min_cost1 = min_cost1, min(min_cost1, min_cost0) + cost
        return min(min_cost0, min_cost1)

def main():
    sol = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(sol.minCostClimbingStairs(cost))


if __name__ == '__main__':
    main()
