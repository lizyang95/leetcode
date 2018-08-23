class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)
        setB = set(B)
        target = (sumA + sumB)//2
        for num in A:
            fromB = target-(sumA-num)
            if fromB in setB and (sumB - fromB + num) == target:
                return [num,fromB]
        return res


sol = Solution()
A = [2]
B = [1,3]
print(sol.fairCandySwap(A,B))
