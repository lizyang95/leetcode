class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board,i,j,word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        res = False
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False

        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        for direction in directions:
            res = res or self.dfs(board,i+direction[0],j+direction[1],word[1:])

        board[i][j] = tmp
        return res


class Solution(object):
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_helper(board, word, i, j):
                    return True
        return False

    def exist_helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = " " # indicate used cell
            # check all adjacent cells
            if i > 0 and self.exist_helper(board, word[1:], i-1, j):
                return True
            if i < len(board)-1 and self.exist_helper(board, word[1:], i+1, j):
                return True
            if j > 0 and self.exist_helper(board, word[1:], i, j-1):
                return True
            if j < len(board[0])-1 and self.exist_helper(board, word[1:], i, j+1):
                return True
            board[i][j] = word[0] # update the cell to its original value
            return False
        else:
            return False


sol = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"

print(sol.exist(board,word))
