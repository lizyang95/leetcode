class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(temperatures)
        stack = []
        for idx,temperature in enumerate(temperatures):
            # print(stack)
            if not stack:
                stack.append(idx)
            else:
                while temperatures[stack[-1]] < temperature:
                    lastindex= stack.pop()
                    ans[lastindex] = idx - lastindex
                    if not stack:
                        stack.append(idx)
                        break
                stack.append(idx)
        return ans

class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in xrange(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans



sol = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(sol.dailyTemperatures(temperatures))
