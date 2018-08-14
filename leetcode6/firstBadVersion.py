class Solution(object):

	#递归的方法
	def firstBadVersion2(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		return self.findBadVersion(1,n)

	def findBadVersion(self,left,right):
		k = (left+right)//2
		if isBadVersion(k):
			if k == 1 or not isBadVersion(k-1):
				return k
			else:
				return self.findBadVersion(left,k-1)
		else:
			if k == right or isBadVersion(k+1):
				return k+1
			else:
				return self.findBadVersion(k+1,right)

	#用template 2，loop 的方法， 因为 我们要寻找第一个bad的值，这就表明，我们要确定，这个bad右侧是bad，这个bad左侧是good的。
	#由于我们保证bad一定存在，所以我们用第二个template
	def firstBadVersion(self,n):
		l,r = 1,n
		while l<r:
			m = (l+r)//2
			#如果当前是bad的，那么第一个bad一定在<=当前的位置
			if isBadVersion(m):
				r = m
			else:
				#如果是good的，那么第一个bad一定>当前的位置
				l = m+1
		return l
