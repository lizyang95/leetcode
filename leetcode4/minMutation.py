class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        import collections
        queue = collections.deque()
        queue.append([start, start, 0]) # current, previous, num_steps
        while queue:
            print(queue)
            current, previous, num_steps = queue.popleft()
            if current == end:  # in BFS, the first instance of current == end will yield the minimum
                return num_steps
            for string in bank:
                if self.getDistance(current, string)==1 and string != previous:
                    queue.append([string, current, num_steps+1])
        return -1


    def getDistance(self,a,b):
        diff = [1 if a[i]!=b[i] else 0 for i in range(len(a))]
        return sum(diff)

sol = Solution()
start = "AAAAACCC"
end =   "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

start = "AACCTTGG"
end = "AATTCCGG"
bank = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
print(sol.minMutation(start,end,bank))
