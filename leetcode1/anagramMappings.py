class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # res = [B.index(A[i]) for i in range(len(A))]
        hashmap = {x:i for i,x in enumerate(B)}
        return [hashmap[x] for x in A]


def main():
    sol = Solution()
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    print(sol.anagramMappings(A,B))

if __name__ == '__main__':
    main()
