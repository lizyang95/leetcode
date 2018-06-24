class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not m:
            for i in range(n):
                nums1[i]=nums2[i]
            print(nums1)
            return
        if not n:
            nums1 = nums1
            print(nums1)
            return

        x = m-1
        y = n-1
        i = m+n-1
        while i >=0:
            if nums1[x]>nums2[y] and x > -1 and y > -1:
                nums1[i]=nums1[x]
                x -= 1
            elif nums1[x]<=nums2[y] and x >-1 and y > -1:
                nums1[i]=nums2[y]
                y -= 1
            elif x==-1:
                nums1[i] = nums2[y]
                y -= 1
            elif y == -1:
                nums1[i] = nums1[x]
                x -= 1
            i -= 1
        print(nums1)





def main():
    sol = Solution()
    # nums1 = [4,5,7,0,0,0]
    # nums1 = [1,2,3,0,0,0]
    # nums2 = [2,5,6]
    # m = 3
    # n = 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    sol.merge(nums1,m,nums2,n)

if __name__ == '__main__':
    main()
