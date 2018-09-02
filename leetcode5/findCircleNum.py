
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        rest = list(range(len(M)))
        stack = [rest[0]]
        ans = 0
        while rest:
            stack = [rest.pop()]
            while stack:
                curr = stack.pop()
                for j in [x for x in rest if M[curr][x] == 1]:
                    rest.remove(j)
                    stack.append(j)
            ans += 1
        return ans
        
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = [0]*len(M)
        count = 0
        from collections import deque
        queue = deque()
        for i in range(len(M)):
            if visited[i]==0:
                queue.append(i)
                while queue:
                    node = queue.popleft()
                    visited[node]=1
                    for j in range(len(M)):
                        if M[node][j]==1 and visited[j]==0:
                            queue.append(j)
                count += 1
        return count



sol = Solution()
M =[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
M = [[1,1,0],[1,1,0],[0,0,1]]
M = [[1,0,0],[0,1,0],[0,0,1]]
M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
for row in M:
    print(row)
print(sol.findCircleNum(M))
