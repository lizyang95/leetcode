
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False

        while(len(matrix)>=1):
            if matrix[-1][-1] < target:
                return False
            else:
                if matrix[-1].count(target) > 0:
                    return True
                else:
                    del matrix[-1]

        return False


    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix:
            return False
        nrow = len(matrix)
        ncol = len(matrix[0])

        r = 0
        c = ncol -1

        while r < nrow and c >=0:
            if target < matrix[r][c]:
                c -= 1
            elif target > matrix[r][c]:
                r += 1
            else:
                return True
        return False
