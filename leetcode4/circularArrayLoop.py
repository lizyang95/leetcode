class Solution(object):

    def move(self,pos,step,n):
        tmp = (pos+step)%n
        return tmp if tmp >=0 else tmp + n

        
def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            count = 0
            pre = i
            isloop = True
            if nums[i] == 0:
                break
            is_forward = nums[i]>0
            while count0) ^ is_forward:# stop if running into a dead end or different sign element
                    isloop = False
                    break
                else:
                    pre = cur
            if isloop:
                return True
            else: # mark all the elements on the wrong path as visited
                pre = i
                while count > 0:
                   cur = (pre+nums[pre])%len(nums)
                   nums[pre] = 0
                   pre = cur
                   count -= 1
        return False

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        a=[]
        an=[]
        for i in xrange(n):
            if i not in a and i not in an:
                j=i
                if nums[j]>0:
                    while j not in a:
                        if nums[j]<0 or j==(j+nums[j])%n:
                            break
                        a.append(j)
                        j=(j+nums[j])%n
                    if j in a:
                        return True
                else:
                    while j not in a:
                        if nums[j]>0 or j==(j+nums[j])%n:
                            break
                        a.append(j)
                        j=(j+nums[j])%n
                    if j in an:
                        return True
        return False



sol = Solution()
nums =  [2, -1, 1, 2, 2]
# nums = [-1,2]
nums = [-2, 1, -1, -2, -2]
nums = [3,1,2]
print(sol.circularArrayLoop(nums))
