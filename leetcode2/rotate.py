class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(0,len(matrix)-1):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(len(matrix)):
            for j in range(int(len(matrix)/2)):
                matrix[i][j],matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1],matrix[i][j]

    def rotate_2(self,matrix):
        matrix[:] = matrix[::-1]
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[i])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
