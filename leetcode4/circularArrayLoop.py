class Solution(object):

    def move(self,pos,step,n):
        tmp = (pos+step)%n
        return tmp if tmp >=0 else tmp + n

    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        visited = []
        visited_values = []
        traveller = 0
        n = len(nums)
        while traveller not in visited:
            visited.append(traveller)
            visited_values.append(nums[traveller])
            traveller = self.move(traveller,nums[traveller],n)
        start = visited.index(traveller)
        print(visited,traveller)
        path = visited[start:]
        step = visited_values[start:]
        if len(path)==1:
            return False
        sig = 1 if step[0]>0 else 0
        for i in range(1,len(step)):
            if sig ==1 and step[i] < 0:
                return False
            if sig == 0 and step[i] > 0:
                return False
        return True





sol = Solution()
nums =  [2, -1, 1, 2, 2]
# nums = [-1,2]
nums = [-2, 1, -1, -2, -2]
nums = [3,1,2]
print(sol.circularArrayLoop(nums))
