class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        # print(nums)
        if nums[0]!=nums[1]:
            res.append(nums[0])
        for i in range(1,len(nums)-1):
            if (nums[i-1]!= nums[i] and nums[i]!= nums[i+1]):
                res.append(nums[i])
        if nums[-2]!=nums[-1]:
            res.append(nums[-1])
        return list(set(res))


class Solution_set(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        st = set()

        for n in nums:
            if n in st:
                st.remove(n)
            else:
                st.add(n)

        return list(st)

sol = Solution()
nums = [1,2,3,2,5]
print(sol.singleNumber(nums))
