class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff = [gas[i] - cost[i] for i in range(len(cost))]
        if sum(diff)<0:
            return -1
        gain = [diff[0]]
        for i in range(len(gas)-1):
            gain.append(diff[i+1]+gain[-1])
        minloc = gain.index(min(gain))
        return (minloc+1)%len(gas)



sol = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(sol.canCompleteCircuit(gas,cost))
