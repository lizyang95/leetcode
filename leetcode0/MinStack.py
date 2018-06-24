class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mindata = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.mindata:
            if self.mindata[-1] > x:
                self.mindata.append(x)
            else:
                self.mindata.append(mindata[-1])
        else:
            self.mindata.append(x)
        self.data.append(x)


    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()
        self.mindata.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return min(self.data)


def main():
# Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    x = 3
    obj.push(x)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()

if __name__ == '__main__':
    main()
