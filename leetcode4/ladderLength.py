class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        import collections
        queue = collections.deque()
        queue.append([beginWord, beginWord, 0]) # current, previous, num_steps
        while queue:
            # print(queue)
            current, previous, num_steps = queue.popleft()
            if current == endWord:  # in BFS, the first instance of current == end will yield the minimum
                return num_steps+1
            for string in wordList:
                if self.getDistance(current, string)==1 and string != previous:
                    queue.append([string, current, num_steps+1])
        return 0


    def getDistance(self,a,b):
        diff = [1 if a[i]!=b[i] else 0 for i in range(len(a))]
        return sum(diff)

sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(sol.ladderLength(beginWord,endWord,wordList))
