import pdb
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # perimeter = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if not grid[i][j]:
        #             continue
        #         ones = 0
        #         if i-1>=0 and grid[i-1][j] == 1:
        #             ones += 1
        #             # print('up')
        #         if i+1<len(grid) and grid[i+1][j]== 1:
        #             ones += 1
        #             # print('down')
        #         if j-1>=0 and grid[i][j-1] == 1:
        #             ones += 1
        #             # print('left')
        #         if j+1<len(grid[0]) and grid[i][j+1] == 1:
        #             ones += 1
        #             # print('right')
        #         perimeter += (4-ones)
        # return perimeter
        h = len(grid)
        w = len(grid[0]) if h else 0

        sum = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    sum += 4
                    if i>0 and grid[i-1][j]:
                        sum -= 2
                    if j >0 and grid[i][j-1]:
                        sum -=2
        return sum


def main():
    sol = Solution()
    grid = [[0,1,0,0],
             [1,1,1,0],
             [0,1,0,0],
             [1,1,0,0]]
    # grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,0,0,0]]

    print(sol.islandPerimeter(grid))

if __name__ == '__main__':
    main()
