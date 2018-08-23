class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1
                count += 1
            if count >=n:
                return True
        return False

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        answer = 0
        zero_trail = 1
        for num in flowerbed:
            if num==0:
                zero_trail += 1
            else:
                if zero_trail >= 3:
                    answer += (zero_trail-1)//2
                    if answer >= n:
                        return True
                zero_trail = 0
        if zero_trail >= 2:
            answer += (zero_trail)//2
        return answer >= n
