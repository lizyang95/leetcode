class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        # people = sorted(people, key=lambda x: x[1])
        # people = sorted(people, key=lambda x: -x[0])
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        # people.sort(key=lambda (h, k): (-h, k))
        # print(people)
        queue = []
        for p in people:
            # print(queue)
            queue.insert(p[1], p)
        return queue


sol = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(sol.reconstructQueue(people))
# expected output = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
