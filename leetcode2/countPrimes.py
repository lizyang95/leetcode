class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        canditates = [i for i in range(2,n)]
        i = 2
        while i<n:
            canditates[::i]= [0 for j in range(len([canditates[::i]]))]
            canditates[i]=i
            i += 1
            print(canditates)





def main():
    sol = Solution()
    print(sol.countPrimes(10))

if __name__ == '__main__':
    main()
