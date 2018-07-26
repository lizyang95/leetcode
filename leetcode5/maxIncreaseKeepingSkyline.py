class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        topdown_view = [ max([ grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]
        # print(topdown_view)
        rightleft_veiw = [max(grid[i][:]) for i in range(len(grid))]
        # print(rightleft_veiw)
        increassum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                increassum += min(rightleft_veiw[i],topdown_view[j]) - grid[i][j]
        return increassum


sol = Solution()
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(sol.maxIncreaseKeepingSkyline(grid))
