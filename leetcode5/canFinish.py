class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        map=[[] for i in range(numCourses)]      #存每个节点的in点
        ind=[0 for i in range(numCourses)]       #存每个节点的out点数

        for p in prerequisites:
            if p[0] not in map[p[1]]:
                map[p[1]].append(p[0])
                ind[p[0]]+=1

        tail=[]                                  #只存0度的节点
        for i in range(numCourses):
            if ind[i]==0:
                tail.append(i)


        count=0

        while tail:
            tmp=tail[0]
            tail.pop(0)                          #弹出0度的节点，数字加1
            count+=1
            for i in map[tmp]:                   #与弹出的节点相连的点，度都－1
                ind[i]-=1
                if ind[i]==0:                    #将度为0的节点存起来
                    tail.append(i)

        if count<numCourses:
            return False
        else:
            return True


class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True

    # BFS: from the end to the front
    def canFinish1(self, numCourses, prerequisites):
        forward = {i: set() for i in xrange(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        queue = collections.deque([node for node in forward if len(forward[node]) == 0])
        while queue:
            node = queue.popleft()
            for neigh in backward[node]:
                forward[neigh].remove(node)
                if len(forward[neigh]) == 0:
                    queue.append(neigh)
            forward.pop(node)
        return not forward  # if there is cycle, forward won't be None

    # BFS: from the front to the end
    def canFinish2(self, numCourses, prerequisites):
        forward = {i: set() for i in xrange(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        queue = collections.deque([node for node in xrange(numCourses) if not backward[node]])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neigh in forward[node]:
                backward[neigh].remove(node)
                if not backward[neigh]:
                    queue.append(neigh)
        return count == numCourses

    # DFS: from the end to the front
    def canFinish3(self, numCourses, prerequisites):
        forward = {i: set() for i in xrange(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        stack = [node for node in forward if len(forward[node]) == 0]
        while stack:
            node = stack.pop()
            for neigh in backward[node]:
                forward[neigh].remove(node)
                if len(forward[neigh]) == 0:
                    stack.append(neigh)
            forward.pop(node)
        return not forward

    # DFS: from the front to the end
    def canFinish(self, numCourses, prerequisites):
        forward = {i: set() for i in xrange(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        stack = [node for node in xrange(numCourses) if not backward[node]]
        while stack:
            node = stack.pop()
            for neigh in forward[node]:
                backward[neigh].remove(node)
                if not backward[neigh]:
                    stack.append(neigh)
            backward.pop(node)
        return not backward


sol = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(sol.canFinish(numCourses,prerequisites))
