class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        return len(A) == len(B) and B in A+A

        if len(A)!=len(B):
            # print(len(A),len(B))
            return False
        if (not len(A)) and (not (len(B))):
            return True
        tmpA = A+A
        for i in range(len(A)):
            # print(tmpA[i:i+(len(A))])
            if B == tmpA[i:i+(len(A))]:
                return True
        return False


A = 'abcde'
B = 'cdeab'
sol = Solution()
print(sol.rotateString(A,B))
