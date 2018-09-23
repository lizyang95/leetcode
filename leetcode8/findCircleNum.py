import pdb

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        cnt, N = 0, len(M)
        vset = set()
        def bfs(n):
            q = [n]
            while q:
                n = q.pop(0)
                for x in range(N):
                    if M[n][x] and x not in vset:
                        vset.add(x)
                        q.append(x)
        for x in range(N):
            if x not in vset:
                cnt += 1
                bfs(x)
        return cnt

    def findCircleNum_DFS(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        cnt, N = 0, len(M)
        vset = set()
        def dfs(n):
            for x in range(N):
                if M[n][x] and x not in vset:
                    vset.add(x)
                    dfs(x)
        for x in range(N):
            if x not in vset:
                cnt += 1
                dfs(x)
        return cnt

sol = Solution()
M =[[1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]]
print(sol.findCircleNum(M))
