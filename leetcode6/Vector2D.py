class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.m=vec2d
        self.rows = len(vec2d)
        self.row, self.col = 0,-1
    def next(self):
        """
        :rtype: int
        """
        return self.m[self.row][self.col]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.m ==[]:
            return False

        if self.col+1<len(self.m[self.row]):
            self.col+=1
            return True

        # find the next available row
        self.row+=1
        while self.row < self.rows and len(self.m[self.row])==0:
            print(self.row)
            self.row+=1

        if self.row<self.rows and len(self.m[self.row])>0:
            self.col=0
            return True
        return False
