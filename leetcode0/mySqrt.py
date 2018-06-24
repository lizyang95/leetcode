class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x or x==1:
            return x
        left = 0
        right = x
        mid = int(left + (right-left)/2)
        while left<=right:
            if x/mid==mid:
                return mid
            elif x/mid>mid:
                left = mid+1
                mid = int(left+(right-left)/2)
            elif x/mid<mid:
                right = mid - 1
                if x/(mid-1)>(mid-1):
                    return mid-1
                mid = int(left + (right-left)/2)



def main():
    sol = Solution()
    x = 1
    print(sol.mySqrt(x))

if __name__ == '__main__':
    main()
