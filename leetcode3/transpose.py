class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for j in range(len(A[0])):
            row = []
            for i in range(len(A)):
                row.append(A[i][j])
            res.append(row)
        return res


sol = Solution()
A = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.transpose(A))
