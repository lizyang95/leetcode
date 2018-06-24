class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        i = 0
        j = len(height)-1
        while i<j:
            area = (j-i)*min(height[i],height[j])
            if maxArea < area:
                maxArea = area
            if height[i]<=height[j]:
                i = i + 1
            else:
                j = j - 1
        return maxArea


def main():
    sol = Solution()
    x = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(x))


if __name__ == '__main__':
    main()
