class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        lev, avail, lev_node = 0, nums, []
        N = len(nums)
        def dfs(lev, avail, lev_node):
            if lev == N:
                res.append(lev_node[:])
                return
            for i in range(len(avail)):
                dfs(lev+1, avail[:i]+avail[i+1:], lev_node+[avail[i]])

        dfs(lev, avail, lev_node)
        return(res)


class Solution_incursive(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        for n in nums:
            print ("n=",n)
            new_perms = []
            for perm in perms:
                print ("perm=",perm)
                for i in xrange(len(perm)+1):
                    print ("i=",i)
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
                    print new_perms
            perms = new_perms
        return perms

def main():
    sol = Solution_incursive()
    print(sol.permute([1,2,3]))

if __name__ == '__main__':
    main()
