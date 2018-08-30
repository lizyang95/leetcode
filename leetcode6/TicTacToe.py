class TicTacToe(object):

    def __init__(self, n):
        self.row = [0] * n
        self.col = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0


    def move(self, row, col, player):
        toAdd = 1 if player == 1 else -1
        n = len(self.row)

        self.row[row] += toAdd
        self.col[col] += toAdd
        if row == col:
            self.diagonal += toAdd
        if row + col == n - 1:
            self.antidiagonal += toAdd
        if abs(self.row[row]) == n or abs(self.col[col]) == n or abs(self.diagonal) == n or abs(self.antidiagonal) == n:
            return player
        return 0
        
