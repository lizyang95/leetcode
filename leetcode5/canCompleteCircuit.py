class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gas.extend(gas)
        cost.extend(cost)
        stops = len(gas)
        print(gas,cost,stops)
        for i in range(stops):
            step = 0
            while step < 

sol = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(sol.canCompleteCircuit(gas,cost))
