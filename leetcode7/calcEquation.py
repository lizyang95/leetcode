class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        import collections
        graph = collections.defaultdict(list)
        for i in range(len(equations)):
            char1,char2 = equations[i][0],equations[i][1]
            graph[char1]=[char2,values[i]]
            graph[char2]=[char1,1.0/values[i]]

        res = []
        for query in queries:
            for char1,char2 in queries:
                stack,seen = [[char1,graph[char1][1]]],{[[char1,graph[char1][1]]]}
                while stack:
                    word = stack.pop()
                    if word == char2:

                        break
                    for nei in graph[char1]:
                        if nei not in seen:
