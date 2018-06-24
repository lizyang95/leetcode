class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {nums[i]:0 for i in range(len(nums))}
        for num in nums:
            if hashmap[num]:
                return True
            else:
                hashmap[num]=1
        return False

class Solution(object):
    def containsDuplicate_withset(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        s = set(nums)
        return len(s) != len(nums)

def main():
    sol = Solution()
    cost = [1,1,1,3,3,4,3,2,4,2]
    # cost =  [1,2,3,4]
    # cost = [1]
    print(sol.containsDuplicate(cost))


if __name__ == '__main__':
    main()
