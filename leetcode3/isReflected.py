class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """

        if len(points) < 2:
            return True
        ylist = []
        for index,point in enumerate(points):
            if point[1] not in ylist:
                ylist.append(point[1])
            print(ylist)
            if len(ylist) > 1:
                return False

        xlist = [point[0] for point in points]
        xlist = list(set(xlist))
        axis = sum(xlist)*1.0/(len(xlist)*1.0)
        xlist.sort()
        right = 0
        left = len(xlist)-1

        dic = {x:2*axis-x for x in xlist}
        for x in xlist:
            if 2*axis-x not in xlist:
                return False

        return True


def main():
    sol = Solution()
    points = [[1,1],[-1,1],[3,1],[2,1]]
    points = [[1,1],[-1,-1]]
    points = [[0,0],[1,0]]
    points = [[-16,1],[16,1],[16,1]]
    print(sol.isReflected(points))

if __name__ == '__main__':
    main()
