class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!=len(B):
            return False
        diff = []
        for i in range(len(A)):
            if A[i]!=B[i]:
                diff.append(i)
        if len(diff) == 0 and len(set(A))<len(A):
            return True
        if len(diff) == 2 and A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
            return True
        return False

        
