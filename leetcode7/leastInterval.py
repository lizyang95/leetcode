class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = {task:tasks.count(task) for task in tasks}
        res = []
        while 1:
            print(counter)
            deletelist = []
            for task in counter:
                if not counter[task]:
                    deletelist.append(task)
            for task in deletelist:
                del counter[task]
            if not len(counter):
                while res[-1] == ' ':
                    res.pop()
                return len(res)
            keys = sorted(counter,key=lambda k:counter[k],reverse=True)
            if len(counter)>=n+1:
                for key in keys[:n+1]:
                    res.append(key)
                    counter[key] -=1
            else:
                for key in keys:
                    res.append(key)
                    counter[key] -= 1
                for i in range(n+1-len(keys)):
                    res.append(' ')

sol = Solution()
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(sol.leastInterval(tasks,n))
