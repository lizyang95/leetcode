class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows.add(i)
                    columns.add(j)
        # print(rows,columns)
        for row in rows:
            matrix[row]=[0]*len(matrix[0])
        # print(matrix)
        for column in columns:
            for row in range(len(matrix)):
                matrix[row][column]=0

    def setZeroes_O1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        if(height ==0): return
        width = len(matrix[0])
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    for tmp in range(height):
                        if matrix[tmp][j] != 0:
                            matrix[tmp][j] = 'a'
                    for tmp in range(width):
                        if matrix[i][tmp] != 0:
                            matrix[i][tmp] = 'a'

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0




sol = Solution()
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

sol.setZeroes(matrix)
print(matrix)
