class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # res = [A[i][::-1] for i in range(len(A))]
        # res = [ [(res[i][j]+1)%2 for j in range(len(A[0]))   ]    for i in range(len(A))]
        # return res

        B = []
        for a in A:
            a = a[::-1]
            a = [b^1 for b in a]
            B.append(a)
        return B


sol = Solution()
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(sol.flipAndInvertImage(A))
