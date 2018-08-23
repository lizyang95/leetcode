class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0]*len(B[0]) for _ in range(len(A))]
        dicA = {i:[] for i in range(len(A[0]))}
        dicB = {i:[] for i in range(len(A[0]))}
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]: dicA[j].append(i)
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j]: dicB[i].append(j)
        for i in range(len(A[0])):
            l1 = dicA[i]
            l2 = dicB[i]
            for m in l1:
                for n in l2:
                    res[m][n]+=A[m][i]*B[i][n]

        return res
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return None

        n1, n2, m1, m2 = len(A), len(A[0]), len(B), len(B[0])

        ans = [[0] * m2 for _ in range(n1)]

        for i, row in enumerate(A):
            for j, a in enumerate(row):
                if a:
                    for k, b in enumerate(B[j]):
                        if b:
                            ans[i][k] += a * b

        return ans


A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ,0 ],
  [ 0, 0, 0 ,0 ],
  [ 0, 0, 1 ,0 ]
]
sol = Solution()
print(sol.multiply(A,B))
