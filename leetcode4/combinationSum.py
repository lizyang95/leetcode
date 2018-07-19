class Solution_dfs:
    def combinationSum_recursive(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        candidates = sorted(candidates)
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return

            for item in candidates:
                if item > remain: break
                if stack and item < stack[-1]: continue
                else:
                    dfs(remain - item, stack + [item])

        dfs(target, [])
        return result

sol = Solution()
candidates = [2,3,6,7]
target = 7
print(sol.combinationSum(candidates,target))
