class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numLen, res, dict = len(num), set(), {}
        if numLen < 4: return []
        num.sort()
        for p in range(numLen):
            for q in range(p+1, numLen):
                if num[p]+num[q] not in dict:
                    dict[num[p]+num[q]] = [(p,q)]
                else:
                    dict[num[p]+num[q]].append((p,q))
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                T = target-num[i]-num[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j: res.add((num[i],num[j],num[k[0]],num[k[1]]))
        return [list(i) for i in res]



class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def binary2sums(nums, target, pre, res):
            n = len(nums)
            if n < 2:
                return
            left, right = 0, n-1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append(pre+[nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < n:
                        if nums[left] == nums[left-1]:
                            left += 1
                        else:
                            break
                    while right > 0:
                        if nums[right] == nums[right+1]:
                            right -= 1
                        else:
                            break
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        def findNsums(nums, target, N, pre, res):
            n = len(nums)
            if N < 2 or N > n:
                return
            if N == 2:
                binary2sums(nums, target, pre, res)
            else:
                if target > nums[-1]*N:
                    return
                for i in range(n-N+1):
                    if nums[i]*N > target:
                        break
                    else:
                        if i == 0 or (i>0 and nums[i]!= nums[i-1]):
                            findNsums(nums[i+1:], target-nums[i], N-1, pre+[nums[i]], res)
        nums.sort()
        res = []
        findNsums(nums, target, 4, [], res)
        return res

sol = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(sol.fourSum(nums,target))
