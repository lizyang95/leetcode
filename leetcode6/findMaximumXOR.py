class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       ans = 0
       for num in nums:
           node = root
           tmp_val = 0
           for j in range (31, -1, -1):
               tmp = num & 1 << j
               if node.one and not tmp: # add when we have 1 ^ 0
                   node = node.one
                   tmp_val += 1 << j
               elif node.zero and tmp: # add when we have 0 ^ 1
                   node = node.zero
                   tmp_val += 1 << j
               else:
                   node = node.one or node.zero
           ans = max(ans, tmp_val)

       return ans
