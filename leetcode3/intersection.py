class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # return list(set(nums1) & set(nums2))
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1.intersection(set2))


class Solution(object):
    def intersect_with_repetation(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res = []
        a = 0
        b = 0
        while a < len(nums1) and b < len(nums2):
            if nums1[a] == nums2[b]:
                res.append(nums1[a])
                a += 1
                b += 1
            elif nums1[a] < nums2[b]:
                a += 1
            else:
                b += 1
        return res

class Solution(object):
    def intersect_with_repetation_dict(self, nums1, nums2):

        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res
