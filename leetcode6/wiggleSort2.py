class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        m = (n+1)>>1
        median = self._kthSmallestNumber(nums,m)

        i,j,k = 0,0,n-1
        while j <=k:
            if nums[self._A(j,n)]>median:
                i += 1
                j += 1
                self._swap(nums,self._A(i,n),self._A(j,n))
            elif nums[self._A(j,n)]<median:
                k -= 1
                self._swap(nums,self._A(j,n),self._A(k,n))
            else:
                j+=1

    def _A(self,i,n):
        return (2*i+1)%(n|1)

    def _swap(self,nums,i,j):
        nums[i],nums[j] = nums[j],nums[i]
        return

    def _kthSmallestNumber(self,nums,m):
        

sol = Solution()
nums = [1, 3, 2, 2, 3, 1]
sol.wiggleSort(nums)
print(nums)
