class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        if(N == 1):
            return nums[0]
        low,high = 0,N-1

        while(low < high):
            mid = low + (high-low)/2
            if(nums[mid] < nums[high]):
                high = mid
            else:
                low = mid + 1

        minidx = low
        low,high = 0,n-1
        while low<=high:
            mid = low + (high-low)/2
            realmid = (mid+minidx)%n
            if nums[realmid]==target:
                return realmid
            if nums[realmid]<target:
                low = mid + 1
            else:
                high = mid-1

        return -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        else:
            start = 0
            end = len(nums)-1

            while (start <= end):
                mid = (start+end)/2

                # If the mid element is the target, return index
                if nums[mid] == target:
                    return mid
                # If not, need to determine the rotation point of the array before dividing up to search
                else:
                    # If the array is rotated in the later half
                    if nums[start] <= nums[mid]:
                        if target >= nums[start] and target < nums[mid]:
                            end = mid - 1
                        else:
                            start = mid + 1
                    # If the array is rotated in the previous half
                    elif nums[mid] < nums[end]:
                        if target > nums[mid] and target <= nums[end]:
                            start = mid + 1
                        else:
                            end = mid - 1
            return -1
