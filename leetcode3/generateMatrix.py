class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for _ in range(n)]
        r,c,di = 0,0,0
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        for i in range(1,n*n+1):
            matrix[r][c]=i
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < n and 0 <= cc < n and matrix[cr][cc]==0:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]

        return matrix
