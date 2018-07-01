class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for char in tokens:
            print(char,stack)
            try:
                stack.append(int(char))
            except:
                a = stack.pop()
                b = stack.pop()
                if char == '+':
                    stack.append(a+b)
                elif char == '-':
                    stack.append(b-a)
                elif char == "*":
                    stack.append(a*b)
                elif char == '/':
                    if b/a >= 0:
                        stack.append(int(b/a))
                    else:
                        stack.append(-1*int(-b/a))

        return stack[0]


def main():
    sol = Solution()
    tokens = ["4","-2","/","2","-3","-","-"]
    print(sol.evalRPN(tokens))

if __name__ == '__main__':
    main()
