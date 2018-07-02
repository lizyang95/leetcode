class Solution_DFS(object):
    def countBattleships(self, board):
        if not board:
            return 0
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        res = 0

        def dfs(board,i,j):
            if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '.' or visited[i][j]):
                return
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            visited[i][j] = 1
            for direction in directions:
                dfs(board,i+direction[0],j+direction[1])

        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board,visited)
                if board[i][j]=='X' and visited[i][j] == 0:
                    res += 1
                    dfs(board,i,j)
        return res




def countBattleships(self, board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                flag = 1
                if j > 0 and board[i][j-1] == 'X': flag = 0
                if i > 0 and board[i-1][j] == 'X': flag = 0
                total += flag
    return total

def main():
    sol = Solution_DFS()
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    print(sol.countBattleships(board))

if __name__ == '__main__':
    main()
