class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # k: distance
        # t: value diff
        
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        if k < 0 or t < 0:
            return False

        bucket = {}

        for i, num in enumerate(nums):
            bucket_id = num / (t+1)
            print(bucket)

            for near_by in (bucket_id - 1, bucket_id, bucket_id + 1):
                if near_by in bucket and abs(bucket[near_by] - num) <= t:
                    return True

            # We don't need to store multiple values in a bucket.
            # Because if that is a case, we should return True above.
            # We always update the bucket with the latest (right most) value.
            bucket[bucket_id] = num

            if i >= k:
                expired = nums[i - k] / (t + 1)
                del bucket[expired]

        return False







sol = Solution()
nums = [1,5,9,1,5,9]
k = 2
t = 3
print(sol.containsNearbyAlmostDuplicate(nums,k,t))
