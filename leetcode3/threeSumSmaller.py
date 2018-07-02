class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        res = 0
        for i in range(n-2):
            prev = res
            tmp_target = target - nums[i]
            l = i+1
            r = n-1
            while l < r:
                tmp = nums[l] + nums[r]
                if tmp < tmp_target:
                    res += r-l
                    l += 1
                else:
                    r -= 1
            if res == prev:
                break
        return res

class Solution_basedontwoSum(object):
    def twoSum(self, A, n):
        if len(A) < 2:
            return 0
        i = 0
        j = len(A) -1
        count =0
        while i< j:
            if A[i] + A[j] < n:
                count += j-i
                i+=1
            else:
                j-=1
        return count

    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        N= sorted(nums)
        count = 0
        for i in range(len(N)):
            count += self.twoSum(N[i+1:],target-N[i])
        return count
