class Solution(object):

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] % 2 == 1:
                    self.helper(board, i, j, m, n)

        for i in range(m):
            for j in range(n):
                nei = board[i][j] // 2
                if (board[i][j] % 2 == 1) and (nei < 2 or nei > 3):
                    board[i][j] += 1
                elif (board[i][j] % 2) == 0 and (nei == 3):
                    board[i][j] += 1
                board[i][j] = board[i][j] % 2

    def helper(self, board, i, j, m, n):
        for x in range(max(i-1,0), min(i+1,m-1)+1):
            for y in range(max(j-1,0), min(j+1,n-1)+1):
                if (x != i) or (y != j):
                    board[x][y] += 2
        

class Solution(object):
    def countneighbours(self,i,j,board):
        up = max(0,i-1)
        down = min(len(board)-1,i+1)
        left = max(0,j-1)
        right = min(len(board[0])-1,j+1)
        neighbours = [board[m][n] if not (m==i and n==j) else 0  for m in range(up,down+1) for n in range(left,right+1)]
        return sum(neighbours)

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        changeFlag = [[False]*len(board[0]) for _ in range(len(board))]
        print(changeFlag)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                liveneighbours = self.countneighbours(i,j,board)
                if board[i][j]:
                    if liveneighbours > 3 or liveneighbours < 2:
                        changeFlag[i][j] = True
                else:
                    if liveneighbours == 3:
                        changeFlag[i][j] = True
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if changeFlag[i][j]:
                    board[i][j] = (board[i][j]+1)%2

sol = Solution()
board =[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]


sol.gameOfLife(board)
print(board)
