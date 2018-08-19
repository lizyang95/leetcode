class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op[0]=='+':
                stack.append(stack[-1]+stack[-2])
            elif op[0]=='C':
                stack.pop()
            elif op[0]=='D':
                stack.append(2*stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        sum = 0
        valid = []

        for string in ops:
            if string not in ['+', 'D', 'C']:
                current_point = int(string)
                valid.append(current_point)
            else:
                if string == '+':
                    last_point = valid.pop()
                    second_last_point = valid.pop()
                    current_point = last_point + second_last_point
                    valid.extend((second_last_point, last_point, current_point))
                elif string == 'D':
                    last_point = valid.pop()
                    current_point = 2 * last_point
                    valid.extend((last_point, current_point))
                else:
                    last_point = valid.pop()
                    current_point = 0
                    sum -= last_point
            sum += current_point

        return(sum)
                
