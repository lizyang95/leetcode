class Solution(object):
    def combine(self, n, k):
        res = []
        stack = []
        x = 1
        while True:
            print(stack)
            if len(stack) == k:
                res.append(stack[:])
            if len(stack) == k or x > n:
                if not stack:
                    return res
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1

    def combine_recursive(self, n, k):
        if k==1:
            return [[i] for i in range(1,n+1)]
        elif k==n:
            return [[i for i in range(1,n+1)]]
        else:
            rs=[]
            rs+=self.combine(n-1,k)
            part=self.combine(n-1,k-1)
            for ls in part:
                ls.append(n)
            rs+=part
            return rs



def main():
    sol = Solution()
    print(sol.combine(4,2))

if __name__ == '__main__':
    main()
