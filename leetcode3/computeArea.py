class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left = max(A,E)
        right = min(G,C)
        bottom = max(F,B)
        top = min(D,H)
        if right > left and top > bottom:
            overlap = (right-left) * (top-bottom)

        return (C-A)*(D-B)+(G-E)*(H-F) - overlap
