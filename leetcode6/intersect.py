class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        result = []
        n = dict()
        for i in nums1:
            if i in n:
                n[i] += 1
            else:
                n[i] = 1

        for i in nums2:
            if i in n and n[i] > 0:
                result.append(i)
                n[i] -= 1

        return result

        
sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(sol.intersect(nums1,nums2))
