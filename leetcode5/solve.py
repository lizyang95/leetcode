class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1) and board[i][j] == 'O':
                    self.dfs(board, i, j)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        if board[i][j] == 'O':
            board[i][j] = 'V'
            if i > 0 and board[i-1][j] == 'O':
                self.dfs(board, i-1, j)
            if j > 1 and board[i][j-1] == 'O':
                self.dfs(board, i, j-1)
            if i < len(board)-1 and board[i+1][j] == 'O':
                self.dfs(board, i+1, j)
            if j < len(board[0])-1 and board[i][j+1] == 'O':
                self.dfs(board, i, j+1)

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        print(m,n)
        from collections import deque
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            while queue:
                posx,posy = queue.popleft()
                board[posx][posy] = 'V'
                for direction in directions:
                    newposx = posx+direction[0]
                    newposy = posy+direction[1]
                    if 0<=newposx<=len(board)-1 and 0<=newposy<=len(board[0])-1 and board[newposx][newposy]=='O':
                        queue.append((newposx,newposy))
            return

        for i in range(n):
            if board[0][i]=='O':
                bfs(0,i)
            if board[m-1][i]=='O':
                bfs(m-1,i)
        printboard(board)
        for i in range(m):
            if board[i][0] == 'O':
                bfs(i,0)
            if board[i][n-1]=='O':
                bfs(i,n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j]=='V':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'



def printboard(board):
    for row in board:
        print(row)

sol = Solution()
board =[
["X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],
["O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","X","X"],
["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","X"],
["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],
["O","O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","X","O","O","X"],
["X","O","O","O","X","O","O","O","O","O","X","O","X","O","X","O","X","O","X","O"],
["O","O","O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O"],
["X","O","O","O","X","X","X","O","X","O","O","O","O","X","X","O","X","O","O","O"],
["O","O","O","O","O","X","X","X","X","O","O","O","O","X","O","O","X","O","O","O"],
["X","O","O","O","O","X","O","O","O","O","O","O","X","X","O","O","X","O","O","X"],
["O","O","O","O","O","O","O","O","O","O","X","O","O","X","O","O","O","X","O","X"],
["O","O","O","O","X","O","X","O","O","X","X","O","O","O","O","O","X","O","O","O"],
["X","X","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],
["O","X","O","X","O","O","O","X","O","X","O","O","O","X","O","X","O","X","O","O"],
["O","O","X","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","X","O"],
["X","X","O","O","O","O","O","O","O","O","X","O","X","X","O","O","O","X","O","O"],
["O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O","O"],
["O","O","O","X","O","O","O","O","O","X","X","X","O","O","X","O","O","O","X","O"],
["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],
["X","O","O","O","O","X","O","O","O","X","X","O","O","X","O","X","O","X","O","O"]
]
sol.solve(board)
printboard(board)
