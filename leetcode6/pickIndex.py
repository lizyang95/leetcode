from random import randint
class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i-1]


    def pickIndex(self):
        """
        :rtype: int
        """
        index = randint(1,self.w[-1])
        start = 0
        end = len(self.w)-1
        if index < self.w[0]:
            return 0
        while start < end:
            mid = (start + end)//2
            if index > self.w[mid]: start = mid + 1
            else: end = mid
        return start



sol = Solution([2,2,2,2,2,2])
print(sol.pickIndex())
