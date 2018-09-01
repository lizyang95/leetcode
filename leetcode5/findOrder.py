class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for i in range(numCourses)]
        ind = [0 for i in range(numCourses)]

        for p in prerequisites:
            if p[0] not in graph[p[1]]:
                graph[p[1]].append(p[0])
                ind[p[0]]+= 1

        tail = [i for i in range(numCourses) if ind[i]==0]

        res = []

        while tail:
            node = tail.pop()
            res.append(node)
            for i in graph[node]:
                ind[i]-=1
                if ind[i]==0:
                    tail.append(i)
        # print(res)
        return res if len(res)==numCourses else []


    def findOrderBFS(self,numCourses,prerequisites):
        # Topological sort works!
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for c1, c2 in prerequisites:
            indegree[c1] += 1
            graph[c2].append(c1)
        q = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for suc in graph[cur]:
                indegree[suc] -= 1
                if indegree[suc] == 0:
                    q.append(suc)
        return res if len(res) == numCourses else []


sol = Solution()
numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]
print(sol.findOrder(numCourses,prerequisites))
